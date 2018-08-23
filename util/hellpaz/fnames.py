#import os
#folder_path = os.getcwd()
#print(folder_path)
#
#import editor
#

#file = os.getcwd() + '/' + os.path.basename(__file__)

import editor

def filepath():

	filepath = editor.get_path()
	return str(filepath)

def filename():
	filename = editor.get_path().split("/")[-1]
	return str(filename)
	
def pathlist():
	path_list = editor.get_path().split("/")
	return path_list

def folderpath():
	folder_path = editor.get_path().split(str(editor.get_path().split("/")[-1]))[0]
	return str(folder_path)

def fall():
	return [filepath(), filename(), pathlist(), folderpath()]





