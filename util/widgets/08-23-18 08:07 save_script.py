#coding: utf-8

''' This script allows you to copy a .py script to the iOS clipboard and then use Open In...
to have that script saved in Pythonista.  This requires both the Workflow and Pythonista apps
and the workflow at https://workflow.is/workflows/8cdee57f79664205a6a565c9cbdb3d48 '''

# Save this script in iphone ~/Documents/save_script.py
# run workflow action extension in safari
# https://workflow.is/workflows/376210099bd84ac6ac4802d5a728424b

import clipboard
import console
import os
import sys
import dialogs
import editor



def save(filename, text, ext):
	root, _ = os.path.splitext(filename)
	extension = ext
	filename = root + extension
	filenum = 1
	while os.path.isfile(filename):
		filename = '{} {}{}'.format(root, filenum, extension)
		filenum += 1
	#print(finalname)
	save_path = str("/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/downloads/scripts/" + filename)
	with open(save_path,'w', encoding='utf-8') as f:
		f.write(text)
	#clipboard.set(filename)
	return filename

def main():
	resp = console.alert('Alert!', 'Choose File Extension', '.py', '.pyui', hide_cancel_button=False)
	if resp==1:
		ext = '.py'
	elif resp==2:
		ext = '.pyui'
	text = clipboard.get()
	assert text, 'No text on the clipboard!'
	filename = dialogs.text_dialog(title="What's your script called?")
	console.clear()
	print('Wait a Moment Please!')
	filename = save(filename.strip().lower().replace(" ","_"), text.strip(), ext)
	console.set_font('Futura', 16)
	save_path = str("/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/downloads/scripts/" + filename)
	print('Done!\nFile Saved as:\n\n' + filename + "\n\nin:\n\n" + save_path)
	editor.open_file(save_path, new_tab=True)

if __name__ == '__main__':
	main()
