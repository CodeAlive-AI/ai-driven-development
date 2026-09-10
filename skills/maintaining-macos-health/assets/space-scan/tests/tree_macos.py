import json,subprocess,tempfile
from pathlib import Path
from integration_macos import fixture,expected
binary=Path(__file__).resolve().parents[1]/'space_scan'
with tempfile.TemporaryDirectory(prefix='tree-scan-') as t:
 root=Path(t).resolve();fixture(root)
 (root/'bystander').mkdir();(root/'bystander/file').write_bytes(b'x'*20)
 for backend in ('bulk','stat'):
  args=[str(binary),'--json','--tree','--top','1','--backend',backend,str(root)]
  p=subprocess.run(args,capture_output=True,text=True,check=True);d=json.loads(p.stdout)
  paths=[];got={}
  for i,(parent,name,logical,allocated,errors,excluded) in enumerate(d['folder_tree']):
   path=name if i==0 else str(Path(paths[parent])/name)
   paths.append(path);got[path]=(logical,allocated)
  assert got==expected(root,True)[1]
  assert len(d['folders'])==1 and len(got)==6
  p=subprocess.run(args+['--exclude',str(root/'b')],capture_output=True,text=True,check=True);d=json.loads(p.stdout)
  assert d['excluded_directories']==1
  assert 'b' not in [r[1] for r in d['folder_tree'][1:]]
  assert 'bystander' in [r[1] for r in d['folder_tree']]
  original=expected(root,True)[1]
  assert d['allocated_bytes']==original[str(root)][1]-original[str(root/'b')][1]
  for bad in (str(root),str(root.parent),'relative'):
   p=subprocess.run(args+['--exclude',bad],capture_output=True,text=True)
   assert p.returncode==1
print('PASS full tree totals and directory-boundary exclusions, both backends')
