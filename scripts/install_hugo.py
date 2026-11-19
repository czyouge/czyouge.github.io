"""Install the pinned official Hugo binary locally and verify its checksum."""
from pathlib import Path
import hashlib, io, platform, tarfile, urllib.request, zipfile

root = Path(__file__).resolve().parents[1]
version = (root/'.hugo-version').read_text().strip()
directory = root/'.tools'
directory.mkdir(exist_ok=True)
system = 'windows' if platform.system() == 'Windows' else 'linux'
filename = f'hugo_{version}_{system}-amd64.' + ('zip' if system == 'windows' else 'tar.gz')
base = f'https://github.com/gohugoio/hugo/releases/download/v{version}/'
target = directory/('hugo.exe' if system == 'windows' else 'hugo')
if target.exists():
    import subprocess
    if ('v'+version) in subprocess.check_output([str(target),'version'], text=True):
        print(target); raise SystemExit(0)
def fetch(name):
    req = urllib.request.Request(base+name, headers={'User-Agent':'czyouge-blog-setup'})
    return urllib.request.urlopen(req, timeout=180).read()
checksums = fetch(f'hugo_{version}_checksums.txt').decode()
expected = next(line.split()[0] for line in checksums.splitlines() if line.split()[-1].lstrip('*') == filename)
data = fetch(filename)
if hashlib.sha256(data).hexdigest() != expected: raise RuntimeError('Hugo checksum mismatch')
if system == 'windows':
    with zipfile.ZipFile(io.BytesIO(data)) as archive: binary = archive.read('hugo.exe')
else:
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive: binary = archive.extractfile('hugo').read()
target.write_bytes(binary)
if system != 'windows': target.chmod(0o755)
print(target)
