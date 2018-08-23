#import os
#folder_path = os.getcwd()
#print(folder_path)
#
#import editor
#

#file = os.getcwd() + '/' + os.path.basename(__file__)

import editor
filepath = editor.get_path()
print("filepath: ", filepath)
print()
filename = editor.get_path().split("/")[-1]
print("filename: ", filename)
print()
path_list = editor.get_path().split("/")
print("folder path as a list: ", path_list)
print()
folder_path = editor.get_path().split(str(editor.get_path().split("/")[-1]))[0]
print("folder path: ", folder_path)
#import os
#inputFilepath = 'path/to/file/foobar.txt'
#filename_w_ext = os.path.basename(inputFilepath)
#filename, file_extension = os.path.splitext(filename_w_ext)
##filename = foobar
##file_extension = .txt
#
#path, filename = os.path.split(path/to/file/foobar.txt)
## path = path/to/file
## filename = foobar.txt



