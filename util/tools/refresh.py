import editor


current_file = editor.get_path()

editor.open_file(current_file, new_tab=False)
