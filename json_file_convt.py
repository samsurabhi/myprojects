## Hello.........Modified file
import json

f1 = open("testjson.json", mode = 'w+')
counter = 0
with open("test.json") as f:
	for line in f:
		if counter == 0 :
			f1.write('[' + line)
			counter = 1
		f1.write(',' + line)
	f1.write(']')
		
with open("testjson.json") as f1:		
	data = json.load(f1)
	for n in data[0]:
		print(n[0])
with open("testjson.json", mode = 'w') as f1:
	json.dump(data, f1, indent = 2 )

#print(data[0]['student'])
#f1.close()

	