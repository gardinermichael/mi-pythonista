import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]

replacement = ''
text_block = ''

if selected_text.strip().startswith('if'):
	for line in selected_text.splitlines():
		if line.strip().startswith('if'):
			replacement += ""
		elif line.strip().startswith('elif'):
			replacement += ""
		elif line.strip().startswith('else:'):
			replacement += ""
		elif line.startswith('\t'):
			replacement += line[line.find('\t') + 1:] + '\n'
		else:
			replacement += line.strip() + '\n'
else:
	for line in selected_text.strip().splitlines():
		text_block += '\t' + line + '\n'
	first_line = selected_text.splitlines()[0]
	tabs = first_line[first_line.find('\t'): first_line.find(first_line.strip())]
	replacement = tabs + "if CONDITION:\n" + text_block + tabs + "elif CONDITION:\n\t\n" + tabs + "else:\n\t"

editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement) - 1)

