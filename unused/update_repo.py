# coding: utf-8
# page title: Working Effectively with Git from iOS
# url: http://codenugget.co/2016/11/20/working-with-git-from-ios.html
# Aug 23, 2018 at 7:38 AM
# 
# 
# 
from collections import OrderedDict
import editor
import re
import sys
from urllib.parse import urlencode, quote
import webbrowser

key = "HM2JYSH833"

def get_path():
	regex= r"\/Documents\/(.+)$"

	path = editor.get_path()
	matches = re.findall(regex, path)
	
	return matches[0]

def get_write_url():
	params = OrderedDict()
	
	params["key"]       = key
	params["x-success"] = "pythonista://"
	params["repo"]      = "mi pythonista"
	params["path"]      = get_path()
	params["text"]      = editor.get_text()
	params["askcommit"] = 1

	return "working-copy://x-callback-url/write/?" + urlencode(params, quote_via=quote)
	
def get_read_url():
	params = OrderedDict()
	
	params["key"]       = key
	params["repo"]      = "py"
	params["path"]      = get_path()
	params["command"]   = "pull"
	params["command"]   = "read"
	params["x-success"] = "pythonista://update_script?action=run&argv={0}&argv=".format(get_path())

	return "working-copy://x-callback-url/chain/?" + urlencode(params, quote_via=quote)

def main():
	if key == "":
		print("You need to fill out key with value from Working Copy settings.")
		quit()
		
	url = get_write_url()
	if len(sys.argv) > 1 and sys.argv[1] == "read":
		url = get_read_url()
	
	webbrowser.open(url)

if __name__ == '__main__':
	main()
