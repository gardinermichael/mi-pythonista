# coding: utf-8
# page title: Working Effectively with Git from iOS
# url: http://codenugget.co/2016/11/20/working-with-git-from-ios.html
# Aug 23, 2018 at 7:39 AM
# 
# 
# 
import editor
import sys

def main():
	print(sys.argv)
	if len(sys.argv) <= 1:
		print("No changes detected.")
		quit()
	
	editor.open_file(sys.argv[1])
	text_length = len(editor.get_text())
	editor.replace_text(0, text_length, sys.argv[2])
	
if __name__ == '__main__':
	main()