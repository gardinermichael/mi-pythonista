from autologging import logged, traced

@logged
@traced
class MyClass:

	def my_method(self, arg, keyword=None):
		self.__log.info("my message")
		return "%s and %s" % (arg, keyword)
		


from pythonjsonlogger import jsonlogger
formatter = jsonlogger.JsonFormatter()


#formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s');
logzero.formatter(formatter)


from logzero import setup_logger

loglogger = setup_logger(name="loglogger", logfile='/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/logfile.log', level=logging.DEBUG)

jsonlogger = setup_logger(name="jsonlogger", logfile="/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/rotating-logfile.json", level=logging.DEBUG, maxBytes=1e6, backupCount=3, disableStderrLogger=True,formatter=jsonlogger.JsonFormatter())

import logging
import logzero
from logzero import logger

# These log messages are sent to the console
logger.debug("hello")
logger.info("info")
logger.warning("warning")
logger.error("error")



# Setup rotating logfile with 3 rotations, each with a maximum filesize of 1MB:
logzero.logfile("/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/rotating-logfile.log", maxBytes=1e6, backupCount=3)

# Set a minimum log level
logzero.loglevel(logging.DEBUG)

# Log messages
logger.info("This log message goes to the console and the logfile")

# This is how you'd log an exception
try:
	raise Exception("this is a demo exception")
except Exception as e:
	logger.exception(e)
	
	
import logging
import sys


targets = logging.StreamHandler(sys.stdout), logging.FileHandler('output.log')

logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M', level=logging.DEBUG, handlers=targets)

logging.debug('testing22')
logging.info('testing23')
print("hello")


import sys

class LoggingPrinter:
	def __init__(self, filename):
		self.out_file = open(filename, "w")
		self.old_stdout = sys.stdout
		#this object will take over `stdout`'s job
		sys.stdout = self
	#executed when the user does a `print`
	def write(self, text):
		self.old_stdout.write(text)
		self.out_file.write(text)
	#executed when `with` block begins
	def __enter__(self):
		return self
	#executed when `with` block ends
	def __exit__(self, type, value, traceback):
		#we don't want to log anymore. Restore the original stdout object.
		sys.stdout = self.old_stdout
		
print("Entering section of program that will be logged.")
with LoggingPrinter("result.txt"):
	print ("I've got a lovely bunch of coconuts.")
print ("Exiting logged section of program.")


import traceback
import sys
from pprint import pprint

def call_function(f, recursion_level=2):
	if recursion_level:
		return call_function(f, recursion_level-1)
	else:
		return f()
		
		
def f():
	return traceback.format_stack()
	
formatted_stack = call_function(f)
pprint(formatted_stack)




print(traceback.format_stack())

print('print_exc() with no exception:', traceback.print_exc(file=sys.stdout))

try:
	raise Exception("trace demo exception")
except Exception:
	print('print_exc():', traceback.print_exc(file=sys.stdout))
	print()
	print('print_exc(1):', traceback.print_exc(limit=1, file=sys.stdout))
	
	
#import traceback
#>>> try:
#...   int('k')
#... except:
#...   var = traceback.format_exc()
#... 
#>>> print var


