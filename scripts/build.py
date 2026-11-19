"""Build a clean production artifact for either existing hostname."""
from pathlib import Path
import os, shutil, subprocess
root = Path(__file__).resolve().parents[1]
host = 'www.czyouge.xyz'
destination = root/'public'
# Only remove our generated output, after checking the final resolved path.
if destination.is_symlink() or destination.resolve().parent != root:
    raise RuntimeError('Output directory must stay directly inside the project')
if destination.exists(): shutil.rmtree(destination)
program = root/'.tools'/('hugo.exe' if os.name == 'nt' else 'hugo')
subprocess.run([str(program),'--gc','--minify','--baseURL',f'https://{host}/','--destination',str(destination)],cwd=root,check=True)
(destination/'CNAME').write_text(host+'\n',encoding='utf-8')
subprocess.run([os.sys.executable,str(root/'scripts/verify.py'),'--public',destination.name,'--host',host],cwd=root,check=True)
