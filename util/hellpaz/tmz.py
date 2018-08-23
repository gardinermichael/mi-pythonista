import time
from datetime import datetime
from pytz import timezone
# define date format
#fmt = '%m-%d-%y %H:%M'
# define eastern timezone
eastern = timezone('US/Eastern')


def tmz():
	fmt = '%m-%d-%y %H:%M'
	loc_dt = datetime.now(eastern)
	dt_str = str(loc_dt.strftime(fmt))
	return dt_str

def hrz():
	fmt = '%H:%M:%S'
	loc_dt = datetime.now(eastern)
	dt_str = str(loc_dt.strftime(fmt))
	return dt_str
	
def daze():
	fmt = '%m-%d-%Y'
	loc_dt = datetime.now(eastern)
	dt_str = str(loc_dt.strftime(fmt))
	return dt_str
	
