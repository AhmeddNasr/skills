"""Offline access to the captured DotCare schema. No database connection or writes."""
import argparse,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/'references'

def read_schema(name):
    path=ROOT/'catalog'/(name+'.json')
    if not path.is_file() or path.parent.resolve()!=(ROOT/'catalog').resolve():
        raise ValueError('Unknown schema: '+name)
    return json.loads(path.read_text(encoding='utf-8'))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--schema');p.add_argument('--table',help='Schema.Table')
    p.add_argument('--readers',help='Schema.Table: SQL objects with captured syntactic references')
    p.add_argument('--object',help='Schema.ViewOrProcedureOrFunction: visible SQL contract/dependencies')
    p.add_argument('--search',help='Table or column name fragment')
    p.add_argument('--neighbors',help='Schema.Table: visible FK and reviewed application links')
    p.add_argument('--required',action='store_true',help='With --table, show nonnullable, nonidentity, noncomputed columns without defaults')
    p.add_argument('--limit',type=int,default=80)
    args=p.parse_args()
    if args.limit<1:raise ValueError('limit must be positive')
    index=json.loads((ROOT/'catalog/index.json').read_text(encoding='utf-8'))
    result=None
    if args.readers:
        if '.' not in args.readers:raise ValueError('Use Schema.Table')
        schema,name=args.readers.split('.',1);hits=[]
        for path in (ROOT/'sql-objects').glob('*.json'):
            if path.name=='index.json':continue
            data=json.loads(path.read_text(encoding='utf-8'))
            for object_name,item in data['Objects'].items():
                deps=[d for d in item['Dependencies'] if str(d.get('referenced_schema_name','')).casefold()==schema.casefold() and str(d.get('referenced_entity_name','')).casefold()==name.casefold()]
                if deps:hits.append({'Object':data['Schema']+'.'+object_name,'Type':item['type_desc'],'References':deps})
        result={'Target':args.readers,'SQLReferences':hits[:args.limit],'TotalMatches':len(hits),'Truncated':len(hits)>args.limit,'Caution':'Syntactic references are not ownership, write direction or delete targets. Check cross-database/server qualification. Dynamic SQL, external code and messages may be absent.'}
    elif args.object:
        if '.' not in args.object:raise ValueError('Use Schema.Object')
        schema,name=args.object.split('.',1)
        path=ROOT/'sql-objects'/(schema+'.json')
        if path.parent.resolve()!=(ROOT/'sql-objects').resolve() or not path.is_file():raise ValueError('Unknown SQL object schema')
        data=json.loads(path.read_text(encoding='utf-8'))
        if name not in data['Objects']:raise ValueError('Unknown SQL object: '+args.object)
        result={'Object':args.object,**data['Objects'][name],'Caution':data['Caution']}
    elif args.table or args.neighbors:
        key=args.table or args.neighbors
        if '.'not in key:raise ValueError('Use Schema.Table')
        schema,table=key.split('.',1);data=read_schema(schema)
        if table not in data['Tables']:raise ValueError('Unknown table: '+key)
        item=data['Tables'][table]
        if args.neighbors:
            extra=json.loads((ROOT/'application-links.json').read_text(encoding='utf-8'))
            result={'Table':key,'DeclaredForeignKeysOut':item['ForeignKeysOut'],'DeclaredForeignKeysIn':item['ForeignKeysIn'],'ReviewedApplicationLinks':[r for r in extra if r['FromTable']==key or r['ToTable']==key],'Caution':'Declared links and reviewed application links have different evidence. Matching column names or numeric IDs are not proof of ownership.'}
        elif args.required:
            result={'Table':key,'RequiredWithoutDefault':[c for c in item['Columns']if c['DataType'].lower() not in ('timestamp','rowversion') and not any(c[k]for k in ['IsNullable','IsIdentity','IsComputed','HasDefault'])],'Caution':'Native validation, configuration and transactional ownership can impose additional requirements.'}
        else:result={'Table':key,**item}
    elif args.search:
        needle=args.search.casefold();hits=[]
        for row in index['Schemas']:
            if args.schema and row['SchemaName']!=args.schema:continue
            data=read_schema(row['SchemaName'])
            for table,item in data['Tables'].items():
                cols=[c['ColumnName']for c in item['Columns']if needle in c['ColumnName'].casefold()]
                if cols or needle in table.casefold():hits.append({'Table':data['Schema']+'.'+table,'MatchingColumns':cols})
        result={'Matches':hits[:args.limit],'TotalMatches':len(hits),'Truncated':len(hits)>args.limit}
    elif args.schema:
        if (ROOT/'catalog'/(args.schema+'.json')).is_file():
            data=read_schema(args.schema);items=[{'Table':args.schema+'.'+name,'Columns':len(t['Columns']),'ApproxRows':t['ApproxRows']}for name,t in data['Tables'].items()]
            result={'Schema':args.schema,'Tables':items[:args.limit],'TableCount':len(items),'Truncated':len(items)>args.limit}
        else:
            path=ROOT/'sql-objects'/(args.schema+'.json')
            if path.parent.resolve()!=(ROOT/'sql-objects').resolve() or not path.is_file():raise ValueError('Unknown schema')
            data=json.loads(path.read_text(encoding='utf-8'));items=[{'Object':args.schema+'.'+name,'Type':t['type_desc']}for name,t in data['Objects'].items()]
            result={'Schema':args.schema,'Objects':items[:args.limit],'ObjectCount':len(items),'TableCount':0,'Truncated':len(items)>args.limit}
    else:result=index
    print(json.dumps(result,ensure_ascii=True,indent=2))

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError)as error:raise SystemExit(str(error))

