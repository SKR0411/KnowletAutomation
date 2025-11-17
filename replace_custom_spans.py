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

# --- Run on all HTML files in current folder ---
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned = replace_custom_spans(content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"✅ Updated spans in: {filename}")