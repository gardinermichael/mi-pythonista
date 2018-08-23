import json
import os
import editor


#file = os.getcwd() + '/' + os.path.basename(__file__)
file = editor.get_path()

#print(file)
parsed = list()
with open(file, 'r') as jsonfile:
	for line in jsonfile:
		parsed.append(json.loads(line))

#print(parsed)	
#print(json.dumps)	
print(json.dumps(parsed, indent=2, sort_keys=True))
	

