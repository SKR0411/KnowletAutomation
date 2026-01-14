import re
import os

first = '''
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5362217555997798"
    crossorigin="anonymous"></script>
</head>
'''

root_dir = '/storage/emulated/0/Workspace/.hidden_workspace/web/knowlet'
# --- Run on all HTML files in current folder ---
for root, _, files in os.walk(root_dir):
  for filename in files:
    if filename.endswith('.html'):
      file_path = os.path.join(root, filename)
      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
      if not '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5362217555997798"' in content:
        cleaned = content.replace('</head>', first)
        #with open(file_path, 'w', encoding='utf-8') as f:
         # f.write(cleaned)
        if content != cleaned:
          print(f"✔️ Updated  in: {root.replace(root_dir, '')}")
        else:
          print(f"🟰 Updated  in: {root.replace(root_dir, '')}")
      else:
        print(f"exists  in: {root.replace(root_dir, '')}")