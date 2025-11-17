import os
import re

rd = "/storage/emulated/0/.hidden_files/workspace/web/knowlet/notes"
total = 0
changed = 0
unchanged = 0
empty = 0
status = 'unknown'
list = []

for root, _, files in os.walk(rd):
  for file in files:
    
    #For Units
    
    if re.match(r"unit_(\d+)\.html", file):
      fp = os.path.join(root, file)
      total += 1
      
      with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
        
      if c == '':
        empty += 1
        status = "empty"
      else:
        if not '<link rel="stylesheet" href="../../../../assets/styles/units.css">' in c:
          nc = c.replace('<style>', '<link rel="stylesheet" href="../../../../assets/styles/units.css">\n    <style>')
          nc = nc.replace('</body>', '    <script src="../../../../assets/scripts/units.js"></script>\n</body>')
          
          if c != nc:
            changed += 1
            status = '✅'
            with open(fp, 'w', encoding='utf-8') as f:
              f.write(nc)
          else:
            unchanged += 1
            status = '🟰'
        else:
          unchanged += 1
          status = '🟰'
        
      print(f"{fp.removeprefix(rd)} {status}")
      
      
print(f"\nTotal: {total}\nEmpty: {empty}\nChanged: {changed}\nUnchanged: {unchanged}")