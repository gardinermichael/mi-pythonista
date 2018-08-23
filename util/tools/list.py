import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]
replacement = '['
for line in selected_text.splitlines():
	if line.strip().startswith("'"):
		replacement += '"' + line + '"' + ","
	else:
		replacement += "'" + line + "'" + ","
replacement += "]"
editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement) - 1)
