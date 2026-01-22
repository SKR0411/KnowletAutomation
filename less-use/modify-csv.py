ROOT_FILE = '/sdcard/.workspace/assets/ratings_rows.csv'

with open(ROOT_FILE, 'r') as r:
	content = r.read()

rows = content.splitlines()
id = 0
newContent = ''
newContent1 = ''
print('0/2')
for row in rows:
	items = row.split(',')
	items[0] = str(id)
	newRow = ','.join(items)
	if (not items[6]):
		newContent += newRow + '\n'
		id += 1
print('1/2')
for row in rows:
	items = row.split(',')
	items[0] = str(id)
	newRow = ','.join(items)
	if (items[6]):
		newContent1 += newRow + '\n'
		id += 1
print('2/2')
with open('/sdcard/.workspace/assets/new_rating_rows.csv', 'w') as w:
	w.write(newContent + newContent1)
print('✅ done')
print(id)