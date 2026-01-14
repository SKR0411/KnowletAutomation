import os 

ROOT_DIR = "/storage/emulated/0/.hidden_workspace/web/knowlet/notes"

tag = '<div class="add-horizontal-scroll">'
count = 0
msg = ""
changed = 0
unchanged = 0
for root, _, files in os.walk(ROOT_DIR):
	for file in files:
		count += 1
		
		if file.endswith(".html"):
			
			file_path = os.path.join(root, file)
			with open(file_path, "r") as r:
				content = r.read()
			
			lines = content.splitlines()
			prev_line = ""
			line_posn = 0
			new_content = ""
			msg = ""
			
			for line in lines:
				line_posn += 1
				new_line = ""
				
				if ("<table>" or "<pre>") in line and not(tag in prev_line):
					
					# print("start at: " + str(line_posn))
					# print(file_path)
					
					new_line = line.replace("<table>", tag + "\n" + line).replace("<pre>", tag + "\n" + line)
					
				elif ("</table>" or "</pre>") in prev_line and not(prev_line.replace("</table>", "</div>").replace("</pre>", "</div>") in line):
					
					# print("end at: " + str(line_posn))
					# print(file_path)
					
					new_line = prev_line.replace("</table>", "</div>\n" + line).replace("</pre>", "</div>\n" + line)
					
				else:
					
					new_line = line
					
				prev_line = line
				new_content += ("\n" if new_content else "") + new_line
				
			if new_content != content:
				with open(file_path, "w") as w:
					w.write(new_content)
				msg = "✔️"
				changed += 1 
			else:
				msg = "🟰"
				unchanged += 1
				
			print(msg + "  " + file_path.replace(ROOT_DIR, ""))
			
		
print("total: " + count)
print("changed: " + changed)
print("unchanged: " + unchanged)