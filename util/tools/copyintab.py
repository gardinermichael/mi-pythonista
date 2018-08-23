import editor
import dialogs
import clipboard
import sys
import console

current_filepath = editor.get_path().split(str(editor.get_path().split("/")[-1]))[0]

text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]

#choose_option = dialogs.list_dialog(items = ["Script", "Clipboard", "Selection"])

choose_option = console.alert('Copy Options', ".py is automatically added", 'Script', 'Clipboard', 'Selection', hide_cancel_button=False)


if choose_option == 3:
	new_content = selected_text
elif choose_option == 2:
	new_content = clipboard.get()
elif choose_option == 1:
	new_content = text
else:
	sys.exit()

#if choose_option == "Selection":
#	new_content = selected_text
#elif choose_option == "Clipboard":
#	new_content = clipboard.get()
#elif choose_option == "Script":
#	new_content = text
#else:
#	sys.exit()

try:
	new_name = str(dialogs.text_dialog(title="New Script Name:", text=current_filepath) + ".py")
	
	editor.make_new_file(new_name, new_content)
	
	editor.open_file(new_name, new_tab=True)
except TypeError:
	sys.exit()
except FileNotFoundError:
	print("To save to iPhone ~/Documents, don't include any file path")
	sys.exit()

