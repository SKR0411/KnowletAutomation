import re
import os

FOLDER_PATH = "/sdcard/.workspace/web/knowlet/notes"
total = 0
changed = 0

for root, _, files in os.walk(FOLDER_PATH):
  for filename in files:
    if re.match(r"unit_(\d+)\.html", filename):
      file_path = os.path.join(root, filename)
      total += 1
  
      # Read the file content
      with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()
        
        # Remove [cite_start]
        html = re.sub(r'\[cite_start\]', '', html)
    
        # Remove [cite: 123] or [cite: 12, 45] or [cite: 1,2,3]
        clean_html = re.sub(r'\[cite:\s*\d+(?:\s*,\s*\d+)*\]', '', html)
        
        if html != clean_html:
          print(file_path.removeprefix(FOLDER_PATH))
          with open(file_path, "w", encoding="utf-8") as w:
            w.write(clean_html)
          changed += 1

print(f'changed: {changed}')