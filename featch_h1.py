import os
import re

FOLDER_PATH = "/sdcard/.workspace/web/knowlet/notes"
status = ""
Total = 0
Correct = 0
Wrong = 0
url = ''
for root, _, files in os.walk(FOLDER_PATH):
  for filename in files:
    if re.match(r"unit_(\d+)\.html", filename):
      file_path = os.path.join(root, filename)
      Total += 1
      url += file_path.replace(FOLDER_PATH, 'https://knowlet.netlify.app/notes').replace('.html', '') + '\n'
      
      
      # Read the file content
      with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        pattern = r'<h1>(.*?)</h1>'
        matches = re.findall(pattern, content)
        
        if re.match(r'Unit (\d+): ', matches[0]):
          Correct+= 1
          status = '✅'
        else:
          Wrong += 1
          status = '❌'
          
        #print(f'{matches[0]} {status}')
with open('url.txt', 'w') as f:
        f.write(url)
print(f'Total: {Total}\nCorrect: {Correct}\nWrong: {Wrong}')
