https://forum.omz-software.com/topic/4826/file-browser-question

import webbrowser
webbrowser.open('pythonista3://Examples')


If your folder name includes characters that aren't allowed in a URL (e.g. spaces), you'll have to percent-encode them using urllib.parse.quote(). If your folder is in iCloud, append ?root=icloud at the end of the URL.



import webbrowser
import os

folder_path = os.path.expanduser('~/Documents/my-folder_01/my-folder_11/my-folder_12/')

content_file = '''
import webbrowser
webbrowser.open('pythonista://.')

'''

with open(folder_path + '.folder.py', 'w') as f:
   f.write(content_file)

webbrowser.open('pythonista://my-folder_01/my-folder_11/my-folder_12/.folder.py?action=run')

import time
time.sleep(0.2)


import os
os.remove(folder_path + '.folder.py')
