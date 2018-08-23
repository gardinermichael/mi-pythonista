import dialogs
import clipboard
import sys
sys.path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/util/hellpaz')
from logg import *
from tmz import *

text = editor.get_text()
s = editor.get_selection()
selection = text[s[0]:s[1]]


if len(selection) > 0:
	clips = str("Clipboard:\n>>> " + clipboard.get() + "\n\nSelection:\n>>> " + selection + "\n\n")
else:
	clips = str("Clipboard:\n>>> " + clipboard.get() + "\n\n")


notes = dialogs.text_dialog(title="Notes", text=clips)

filename = editor.get_path().split("/")[-1]

folder_path = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/notes/'

subfilepath = str(folder_path + filename + " - notes.md")


with LoggingPrinter(submodule=subfilepath):
	print("####note")
	print()
	print("+ **datetime:** ", tmz())
	print("+ **notes:**")
	print()
	print("\t\t" + notes)
	print("_____")
	sys.exit()

