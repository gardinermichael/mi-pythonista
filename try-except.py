import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]

replacement = ''
text_block = ''
error_handling = 'with Loge(e):\n\t'
pass_handling = '\tpass'

if selected_text.strip().startswith('try:'):
	for line in selected_text.splitlines():
		if line.strip().startswith('try:'):
			replacement += ""
		elif line.strip().startswith('except'):
			replacement += ""
		elif line.strip().startswith('with Loge(e):'):
			replacement += ""
		elif line.strip().startswith('pass'):
			replacement += ""
		elif line.startswith('\t'):
			replacement += line[line.find('\t') + 1:] + '\n'
		else:
			replacement += line.strip() + '\n'
else:
	for line in selected_text.splitlines():
		text_block += '\t' + line + '\n'
	first_line = selected_text.splitlines()[0]
	tabs = first_line[first_line.find('\t'): first_line.find(first_line.strip())]
	replacement = tabs + "try:\n" + text_block + tabs + "except Exception as e:\n\t" + tabs + error_handling + tabs + pass_handling

editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement) - 1)

