import os
import re

total_files = 0
html_files = 0

unit = 0
paper = 0
subject = 0
semester = 0

rd = '/storage/emulated/0/.hidden_workspace/web/Knowlet/notes'

for root, _, files in os.walk(rd):
  for filename in files:
    total_files += 1
    if filename.endswith('.html'):
      html_files += 1
      
      file_path = os.path.join(root, filename)
      
      if re.search(r'unit_(\d+)\.html', file_path):
        unit += 1
      elif re.search(r'semester_(\d+)\.html', file_path):
        semester += 1
      elif re.search(r'([a-z_]+)\.html', file_path):
        subject += 1
      elif re.search(r'([a-z]{3})_(\d+)\.html', file_path):
        paper += 1
        
folder_count = sum(len(dirs) for _, dirs, _ in os.walk(rd))

print(f'Total Files: {total_files}')
print(f'HTML Files: {html_files}')
print(f'Folders: {folder_count}')

print(f'\nUnit: {unit}')
print(f'Paper: {paper}')
print(f'Subject: {subject}')
print(f'Semester: {semester}')