# encoding='utf-8'

import os,glob
folder_path = os.getcwd()



folder_path += "/texas_bar/"

print(folder_path)


for filename in os.listdir(folder_path):
    print (filename)
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        print (filename)
        print (len(text))
 


#for filename in glob.glob(os.path.join(folder_path, '*.htm')):
#    with open(filename, 'r') as f:
#        text = f.read()
#        print (filename)
#        print (len(text))


foldername = editor.get_path().split("/")[-2]
