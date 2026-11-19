"""Verify the published URL contract and Markdown import without third-party packages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import argparse, json, xml.etree.ElementTree as ET

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.assets, self.refresh = set(), [], False
        self.avatar = None
        self.feed(text)
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'img' and 'brand-avatar' in a.get('class', '').split(): self.avatar = a.get('src')
        if tag in ('img', 'source', 'video', 'script') and a.get('src'): self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet': self.assets.append(a['href'])
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh': self.refresh = True

def output_file(root, path):
    target = root / unquote(path).lstrip('/')
    if path.endswith('/') or not target.suffix: target /= 'index.html'
    return target

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', default='public')
    parser.add_argument('--host', default='www.czyouge.xyz')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    public = root / args.public
    failures = []
    homepage = Document((public/'index.html').read_text(encoding='utf-8'))
    avatar_path = urlsplit(homepage.avatar or '').path
    if not avatar_path or avatar_path.startswith('/blog/'):
        failures.append('Avatar must be published outside the retired /blog/ project route')
    else:
        avatar_file = public/unquote(avatar_path).lstrip('/')
        if not avatar_file.is_file() or avatar_file.read_bytes() != (root/'static/blog/avatar.png').read_bytes():
            failures.append('Published avatar does not match static/blog/avatar.png')
    cname = public/'CNAME'
    if not cname.exists() or cname.read_text(encoding='utf-8').strip() != args.host:
        failures.append('Incorrect CNAME for ' + args.host)
    for entry in ('post/goodstuff/index.html',):
        if (public/entry).exists(): failures.append('Local-only draft was published: ' + entry)
    inventory = json.loads((root/'data/legacy_urls.json').read_text(encoding='utf-8'))
    # Both former sites now live under the single primary hostname.
    routes = list({x['path']: x for x in inventory}.values())
    anchor_count = 0
    for entry in routes:
        target = output_file(public, entry['path'])
        if not target.is_file(): failures.append('Missing URL: ' + entry['path']); continue
        doc = Document(target.read_text(encoding='utf-8'))
        if entry['kind'] == 'article' and doc.refresh: failures.append('Article redirects: ' + entry['path'])
        for anchor in entry['ids']:
            anchor_count += 1
            if anchor not in doc.ids: failures.append('Missing anchor: ' + entry['path'] + '#' + anchor)
    for file in public.rglob('*.html'):
        doc = Document(file.read_text(encoding='utf-8'))
        for value in doc.assets:
            url = urlsplit(value)
            if url.scheme in ('data', 'blob'): continue
            if url.netloc and url.netloc not in ('www.czyouge.xyz','blog.czyouge.xyz','czyouge.github.io','czyouge.xyz'): continue
            target = public/unquote(url.path).lstrip('/') if url.path.startswith('/') else file.parent/unquote(url.path)
            if not target.is_file(): failures.append('Missing asset: ' + str(file.relative_to(public)) + ' -> ' + value)
    for name in ('atom.xml', 'rss.xml', 'sitemap.xml'):
        try: ET.parse(public/name)
        except Exception as error: failures.append('Invalid feed: ' + name + ': ' + str(error))
    search = json.loads((public/'index.json').read_text(encoding='utf-8'))
    expected = []
    for file in (root/'content/posts').glob('*.md'):
        if file.name == '_index.md': continue
        text = file.read_text(encoding='utf-8')
        _, front, body = text.split('---',2)
        if '\ndraft: true' not in '\n'+front and '\nhidden: true' not in '\n'+front: expected.append(file)
    if len(search) != len(expected): failures.append(f'Search count {len(search)} != published articles {len(expected)}')
    known = {item['url'] for item in search}
    if len(known) != len(search): failures.append('Duplicate search URLs')
    if any(urlsplit(item['url']).netloc == 'blog.czyouge.xyz' for item in search):
        failures.append('Search still sends readers to the retired hostname')
    print(f'Checked {len(routes)} legacy URLs, {anchor_count} legacy anchors, {len(search)} searchable articles, local assets and XML feeds.')
    for message in sorted(set(failures)): print('FAIL:', message)
    if failures: return 1
    print('PASS')
    return 0

if __name__ == '__main__': raise SystemExit(main())
