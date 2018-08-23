# coding: utf-8
import appex
from markdown2 import markdown
import ui
import editor

TEMPLATE = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>Preview</title>
<style type="text/css">
body {
	font-family: helvetica;
	font-size: 15px;
	margin: 10px;
}
</style>
</head>
<body>{{CONTENT}}</body>
</html>
'''

def main():

	filename = editor.get_path()
	with open(filename, 'r', encoding='utf-8') as f:
		text = f.read()
	
	if not text:
		print('No input text found. Use this script from the share sheet in an app like Notes.')
		return
	converted = markdown(text)
	html = TEMPLATE.replace('{{CONTENT}}', converted)
	webview = ui.WebView(name='Markdown Preview')
	webview.load_html(html)
	webview.present()

if __name__ == '__main__':
	main()
