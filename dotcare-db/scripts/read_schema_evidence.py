import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--kind',choices=['samples','setup-vocabularies'],required=True);p.add_argument('--schema',required=True);a=p.parse_args()
d=json.loads((Path(__file__).resolve().parents[1]/'references'/(a.kind+'-bundle.json')).read_text(encoding='utf-8'))
if a.schema not in d:p.error('No captured evidence for requested schema')
print(json.dumps(d[a.schema],indent=2,ensure_ascii=True))
