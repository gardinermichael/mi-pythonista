from shutil import copytree
import editor

import time
from datetime import datetime
from pytz import timezone
# define date format
fmt = '%m-%d-%y %H:%M'
# define eastern timezone
eastern = timezone('US/Eastern')
loc_dt = datetime.now(eastern)
dt_str = str(loc_dt.strftime(fmt))

parents = " from: " + editor.get_path().split("/")[-3] + " in " + editor.get_path().split("/")[-4]
foldername = editor.get_path().split("/")[-2]

copyfolderpath = "/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/copies/folders/" + dt_str + " " + foldername + parents


org_folder = '/'.join(editor.get_path().split('/')[:-1])


if (editor.get_path().split('/')[-2] == 'Documents'):
    print('Cannot copy Documents folder')
else:
    copytree(org_folder, copyfolderpath)

print(copyfolderpath)

# https://forum.omz-software.com/topic/4560/copyfile-action
