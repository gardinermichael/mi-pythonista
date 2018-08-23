# Search StackOverflow for selected text

import editor
import webbrowser
import dialogs
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
search_url = 'http://google.com/search?tbs=qdr:y&q='

if len(selection) > 0:
	query = urllib.parse.quote(selection)
else:
	selection = dialogs.text_dialog(title="Past Year Google Search", text=clips)
	query = urllib.parse.quote(selection)


filename = editor.get_path().split("/")[-1]

folder_path = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/notes/'

subfilepath = str(folder_path + filename + " - notes.md")

with LoggingPrinter(submodule=subfilepath):
	print("####past year google search")
	print()
	print("+ **datetime:** ", tmz())
	print("+ **g.query:** ", str("[" + selection + "](" + search_url+query + ")"))
	print("_____")
	webbrowser.open(str(search_url+query))
	sys.exit()

