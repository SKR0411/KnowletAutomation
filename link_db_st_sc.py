import os
import re

rd = "/storage/emulated/0/.hidden_workspace/web/knowlet/notes"
total = 0
changed = 0
unchanged = 0
empty = 0
status = 'unknown'

for root, _, files in os.walk(rd):
  for file in files:
    
    #For Units
    
    if re.match(r"unit_(\d+)\.html", file):
      fp = os.path.join(root, file)
      total += 1
      
      with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
        
      nc = c
    
      #link Styles
      if not '<link rel="stylesheet"' in c:
        nc = c.replace('<style>','''<link rel="stylesheet" href="../../../../assets/styles/units.css">
    <link rel="stylesheet" href="../../../../assets/styles/supabase.css">
    <style>''')
      
      #link scripts
      if not '<div id="app"></div>' in c:
        nc = nc.replace('</body>','''<div id="app"></div>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <script src="../../../../assets/scripts/units.js"></script>
</body>
''')
        
      if c != nc:
        with open(fp, 'w', encoding='utf-8') as f:
          f.write(nc)
        changed += 1
        status = '✔️'
      else:
        unchanged += 1
        status = '🟰'
    
      print(f"{status} {fp.removeprefix(rd)}")
      
      
print(f"\nTotal: {total}\nEmpty: {empty}\nChanged: {changed}\nUnchanged: {unchanged}")