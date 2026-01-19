import re
import os

FOLDER_PATH = "/sdcard/.workspace/web/knowlet/notes"
total = 0
yes = 0
no = 0
htmlclone = ''


def addintend(html):
    lines = html.splitlines()
    newhtml = ''
    isInside = False
    isInsideLast = False

    for line in lines:
        #print(line)
        if line == '<div class="container">':
            #print(line)
            isInside = True

        if line == '</div>':
            #print(line)
            isInside = False

        #print(isInside)

        if isInside:
            newhtml += "    " + line + "\n"
        else:
            if isInsideLast:
                newhtml += "    " + line + "\n"
            else:
                newhtml += line + "\n"

        isInsideLast = isInside

    #print(newhtml)
    return newhtml

for root, _, files in os.walk(FOLDER_PATH):
    for filename in files:
        if re.match(r"unit_(\d+)\.html", filename):
            file_path = os.path.join(root, filename)
            total += 1
    
            # Read the file content
            with open(file_path, "r", encoding="utf-8") as file:
                html = file.read()
                
            if '    <div class="container">' in html:
                #print('yes ' + file_path.removeprefix(FOLDER_PATH))
                yes += 1;
            else:
                #If not exist
                if '<div class="container">' in html:
                    print('no ' + file_path.removeprefix(FOLDER_PATH))
                    no += 1;
                    newhtml = addintend(html)
                    with open(file_path, 'w') as w:
                        w.write(newhtml)
                    #htmlclone = html

#addintend(htmlclone)
print(f'total: {total}\nyes: {yes}\nno: {no}')