import re
import os

def replace_custom_spans(text):
  """
  Converts [span_X](start_span)...[span_X](end_span)
  into <span id="span_X">...</span>
  """
  pattern = re.compile(r'\[span_(\d+)\]\(start_span\)(.*?)\[span_\1\]\(end_span\)', re.DOTALL)
  replaced = re.sub(pattern, r'<span id="span_\1">\2</span>', text)
  return replaced

root_dir = '/sdcard/.workspace/web/knowlet/notes'
# --- Run on all HTML files in current folder ---
for root, _, files in os.walk(root_dir):
  for filename in files:
    if re.match(r"unit_(\d+)\.html", filename):
      file_path = os.path.join(root, filename)
      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
      cleaned = replace_custom_spans(content)
      #with open(file_path, 'w', encoding='utf-8') as f:
       # f.write(cleaned)
      if content != cleaned:
        print(f"✔️ Updated spans in: {root.replace(root_dir, '')}")