"""Create a draft with a permanent URL; only the Python standard library is needed."""
from pathlib import Path
from datetime import datetime
import json, re
root = Path(__file__).resolve().parents[1]
title = input('Article title: ').strip()
slug = input('Permanent URL ID (English letters, numbers and hyphens): ').strip()
if not title or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug): raise SystemExit('Invalid title or URL ID.')
created = datetime.now().astimezone()
path = root/'content/posts'/(created.strftime('%y%m')+'-'+slug+'.md')
url = '/post/'+slug+'/'
for file in (root/'content').rglob('*.md'):
    if url in file.read_text(encoding='utf-8').split('---',2)[1]: raise SystemExit('This URL is already in use.')
if path.exists(): raise SystemExit('File already exists.')
date = created.isoformat(timespec='seconds')
text = f'---\ntitle: {json.dumps(title,ensure_ascii=False)}\ndate: {date}\nurl: {url}\ntags: []\ndraft: true\n---\n\n'
path.write_text(text,encoding='utf-8')
print(path)
