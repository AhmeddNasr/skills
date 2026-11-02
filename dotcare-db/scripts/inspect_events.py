"""Find source event subscription candidates; no broker connection or execution."""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--event',default='');p.add_argument('--module',default='');p.add_argument('--include-commented',action='store_true');a=p.parse_args()
d=json.loads((Path(__file__).resolve().parents[1]/'references/event-subscriptions.json').read_text(encoding='utf-8'))
r=[x for x in d['Entries']if a.event.casefold()in x['MessageType'].casefold()and a.module.casefold()in x['ModuleDirectory'].casefold()and(a.include_commented or not x['CommentedDeclaration'])]
print(json.dumps({'Matches':r,'Count':len(r),'Caution':d['Caution']},indent=2,ensure_ascii=True))
