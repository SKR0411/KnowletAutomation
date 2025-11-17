import os
import re

folder_path = "/storage/emulated/0/.hidden_files/workspace/web/Knowlet/notes"
total = 0
for root, _, files in os.walk(folder_path):
  for filename in files:
    if re.match(r"unit_(\d+)\.html", filename):
      file_path = os.path.join(root, filename)
      
      with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        new_content = content
        pattern = r'\<title>(.*?)\</title>'
        matches = re.findall(pattern, content)
        print(matches[0])
        total += 1
print(f'Total: {total}')