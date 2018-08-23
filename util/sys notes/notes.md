import sys
sys.path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/util/hellpaz')
from logg import *
from tmz import *
from fnames import *

__________________________________________________

with LoggingPrinter(filename="result.txt", terms="search"):
	print()

try:
	raise Exception("this is a demo exception")
except Exception as e:
	with Loge(e):
		pass

tmz()
hrz()
daze()

fall(), filepath(), filename(), pathlist(), folderpath()

__________________________________________________

folder_path = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/'


__________________________________________________

# coding: utf-8

#! python2
#! python3

__________________________________________________

html = open(file_path, 'r', encoding='utf-8')

with open(save_path,'a', encoding='utf-8') as f:
with open(save_path,'w', encoding='utf-8') as f:
		f.write(text)

__________________________________________________

filename = editor.get_path().split("/")[-1]

foldername = editor.get_path().split("/")[-2]

folder_path = editor.get_path().split(str(editor.get_path().split("/")[-1]))[0]

__________________________________________________

if __name__ == '__main__':
	main()
	
	
__________________________________________________
	
import time
time.sleep(0.2)
	
	
