import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]
replacement = ""
duplicates = list()

for line in selected_text.splitlines():
	if line in duplicates:
		pass
	else:
		replacement += line + "\n"
		duplicates.append(line)
		
	
editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement) - 1)
