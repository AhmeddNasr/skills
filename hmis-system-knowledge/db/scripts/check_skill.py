import json,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def run(*args):
 p=subprocess.run([sys.executable,str(root/'scripts/inspect_schema.py'),*args],capture_output=True,text=True)
 assert p.returncode==0,p.stderr
 return json.loads(p.stdout)
i=run();assert i['SchemaCount']==44 and i['TableCount']==2042
assert sum(len(json.loads(p.read_text(encoding="utf-8"))['Tables']) for p in (root/'references/catalog').glob('*.json') if p.name!='index.json')==2042
r=run('--table','VisitMgt.VisitPackagesAssignment','--required')
assert not any(c['DataType'].lower() in ('timestamp','rowversion') for c in r['RequiredWithoutDefault'])
p=run('--table','Billing.PatientPackage');idcol=next(c for c in p['Columns'] if c['ColumnName']=='ID');assert not idcol['IsIdentity']
r=run('--neighbors','VisitMgt.VisitPackagesAssignment');links=r['ReviewedApplicationLinks'];assert any(x['ToTable']=='VisitMgt.VisitService' for x in links)
r=run('--search','ID','--limit','1');assert r['Truncated'] and len(r['Matches'])==1
p=subprocess.run([sys.executable,str(root/'scripts/inspect_schema.py'),'--table','../missing.X'],capture_output=True,text=True);assert p.returncode!=0
for name in ['module-map.md','core-flows.md','review-procedure.md','migration-conventions.md','module-source-findings.md']:assert (root/'references'/name).is_file()
print('PASS: catalog totals, generated-column exclusion, shared key, reviewed package link, truncation, invalid lookup and guidance references')


# Additional behavior checks: do not conflate referenced setup and dependent records.
def trace(*args):
 p=subprocess.run([sys.executable,str(root/'scripts/trace_dependencies.py'),*args],capture_output=True,text=True)
 assert p.returncode==0,p.stderr
 return json.loads(p.stdout)
x=trace('--root','Security.User','--depth','1','--direction','incoming')
assert 'Security.UserRole' in [n['Table'] for n in x['Nodes']]
y=trace('--root','Security.User','--depth','1','--direction','outgoing')
assert 'Security.Entity' in [n['Table'] for n in y['Nodes']]
assert 'Security.UserRole' not in [n['Table'] for n in y['Nodes']]
z=trace('--root','VisitMgt.Visit','--depth','0');assert len(z['Nodes'])==1 and not z['DeclaredEdges']
z=trace('--root','VisitMgt.Visit','--depth','2','--limit','2');assert len(z['Nodes'])==2 and z['TruncatedByLimit']
assert len(list((root/'references/schemas').glob('*.md')))==48
coverage=json.loads((root/'references/domain-coverage.json').read_text(encoding='utf-8'));assert sum(x['Tables']for x in coverage)==2042
print('PASS: direction-sensitive impact graph, boundary/limit handling and all-table three-domain worksheet coverage')

assert run('--schema','BIReport')['TableCount']==0
assert run('--object','PatientSummery.VWPSGetAllergiesPerVisit')['type_desc']=='VIEW'
assert run()['ForeignKeyConstraints']==2132
coverage=json.loads((root/'references/sample-coverage.json').read_text(encoding='utf-8'));assert coverage['TableCount']==2042 and coverage['AllTableSamplingComplete'] and not coverage['BusinessFlowVerificationComplete']
print('PASS: view-only schema access, SQL object contracts, schema-scoped constraint count and honest sampling status')

r=run('--readers','Allergy.PatientAllergyTransaction','--limit','1000');assert any(x['Object']=='PatientSummery.VWPSGetAllergiesPerVisit'for x in r['SQLReferences'])
print('PASS: reverse SQL references identify derived displays separately from owned children')
