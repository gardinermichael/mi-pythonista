# Search StackOverflow for selected text

import editor
import webbrowser
#
#text = editor.get_text()
#s = editor.get_selection()
#selection = text[s[0]:s[1]]
#if len(selection) > 0:
#	import urllib.parse
#	q = urllib.parse.quote(selection)
#	search_url = 'http://stackoverflow.com/search?q=' + q
#	webbrowser.open(search_url)
#else:
#	from console import alert
#	i = alert('No Selection', 'Do you want to open the StackOverflow homepage?', 'StackOverflow')
#	if i == 1:
#		webbrowser.open('http://stackoverflow.com')



import dialogs
import editor
import clipboard
import sys
sys.path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/util/hellpaz')
from logg import *
from tmz import *

import urllib.parse

clips = str(clipboard.get())
text = editor.get_text()
s = editor.get_selection()
selection = text[s[0]:s[1]]
search_url = 'http://stackoverflow.com/search?q='

if len(selection) > 0:
	query = urllib.parse.quote(selection)
else:
	selection = dialogs.text_dialog(title="Stack Overflow Search", text=clips)
	query = urllib.parse.quote(selection)
	
filename = editor.get_path().split("/")[-1]

folder_path = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/notes/'

subfilepath = str(folder_path + filename + " - notes.md")

with LoggingPrinter(submodule=subfilepath):
	print("####stack overflow search")
	print()
	print("+ **datetime:** ", tmz())
	print("+ **so.query:** ", str("[" + selection + "](" + search_url+query + ")"))
	print("_____")
	webbrowser.open(str(search_url+query))
	sys.exit()
