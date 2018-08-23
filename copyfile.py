from shutil import copyfile
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


filename = editor.get_path().split("/")[-1]

copyfolderpath = "/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/copies/" + dt_str + " " + filename

print(copyfolderpath)


copyfile(editor.get_path(),copyfolderpath)

#copyfile(editor.get_path(),editor.get_path().split(".")[0].split("/")[-1]+'.copy')



# https://forum.omz-software.com/topic/4560/copyfile-action
