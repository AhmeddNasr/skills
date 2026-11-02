"""Inspect declared FK reachability and reviewed application links offline; not a deletion planner."""
import argparse,json
from pathlib import Path
from collections import deque
ROOT=Path(__file__).resolve().parents[1]/'references'
def graph():
 nodes=set();edges=[];seen=set()
 for path in (ROOT/'catalog').glob('*.json'):
  if path.name=='index.json':continue
  data=json.loads(path.read_text(encoding='utf-8'))
  for table,item in data['Tables'].items():
   nodes.add(data['Schema']+'.'+table)
   for f in item['ForeignKeysOut']:
    child=f['ChildSchema']+'.'+f['ChildTable'];parent=f['ParentSchema']+'.'+f['ParentTable'];key=(child,parent,f['ConstraintName'])
    if key in seen:continue
    seen.add(key);group=[x for x in item['ForeignKeysOut']if x['ConstraintName']==f['ConstraintName']]
    edges.append({'Child':child,'Parent':parent,'Evidence':'declared FK','Name':f['ConstraintName'],'Columns':[{'Child':x['ChildColumn'],'Parent':x['ParentColumn'],'Ordinal':x['Ordinal']}for x in sorted(group,key=lambda x:x['Ordinal'])],'OnDelete':f['OnDelete'],'OnUpdate':f['OnUpdate'],'Disabled':f['IsDisabled'],'Untrusted':f['IsNotTrusted']})
 return nodes,edges

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',required=True,help='Schema.Table');p.add_argument('--depth',type=int,default=2);p.add_argument('--limit',type=int,default=100);p.add_argument('--direction',choices=['incoming','outgoing','both'],default='incoming');a=p.parse_args()
 if not 0<=a.depth<=8 or not 1<=a.limit<=1000:raise ValueError('depth must be 0..8 and limit 1..1000')
 nodes,edges=graph()
 if a.root not in nodes:raise ValueError('Unknown root table')
 adjacency={n:[]for n in nodes}
 for e in edges:
  if a.direction in ('incoming','both'):adjacency[e['Parent']].append((e['Child'],e))
  if a.direction in ('outgoing','both'):adjacency[e['Child']].append((e['Parent'],e))
 reached={a.root:0};queue=deque([a.root]);truncated=False;result=[];edgekeys=set()
 while queue:
  n=queue.popleft()
  if reached[n]>=a.depth:continue
  for target,e in adjacency[n]:
   if target not in reached:
    if len(reached)>=a.limit:truncated=True;continue
    reached[target]=reached[n]+1;queue.append(target)
   key=(e['Child'],e['Parent'],e['Name'])
   if key not in edgekeys:result.append(e);edgekeys.add(key)
 apps=json.loads((ROOT/'application-links.json').read_text(encoding='utf-8'))
 print(json.dumps({'Root':a.root,'Direction':a.direction,'Depth':a.depth,'Nodes':[{'Table':n,'Depth':d}for n,d in reached.items()],'DeclaredEdges':result,'TruncatedByLimit':truncated,'ReviewedApplicationLinksTouchingNodes':[e for e in apps if e['FromTable']in reached or e['ToTable']in reached],'Caution':'FK reachability is not ownership, affected-row discovery or deletion order. Application links are reported separately and are not traversed. Unrecorded polymorphic links, caches, triggers, jobs and external effects can remain. Boundary nodes may have further dependencies.'},ensure_ascii=True,indent=2))
if __name__=='__main__':
 try:main()
 except ValueError as error:raise SystemExit(str(error))

