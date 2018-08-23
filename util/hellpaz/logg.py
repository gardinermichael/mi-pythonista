import sys
import editor 


#import sys
#sys.path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/util/hellpaz/')
#from logg import *


#from logg import LoggingPrinter,Loge

class LoggingPrinter:
	scriptname = editor.get_path().split("/")[-1]
	
	def __init__(self, filename = str("/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/" + scriptname + " - " + "logged_printer.txt"), submodule = None):
		
		if submodule != None:
			filename = str(submodule)
			self.out_file = open(filename, "a")
		else:
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
		
#print("Entering section of program that will be logged.")
#with LoggingPrinter(filename="result.txt", terms="search"):
#       print ("I've got a lovely bunch of coconuts.")

#try:
#	raise Exception("this is a demo exception")
#except Exception as e:
#	with Loge(e):
#		pass



import logging
from pythonjsonlogger import jsonlogger


supported_keys = [
	'asctime',
	'created',
	'filename',
	'funcName',
	'levelname',
	'levelno',
	'lineno',
	'module',
	'msecs',
	'message',
	'name',
	'pathname',
	'process',
	'processName',
	'relativeCreated',
	'thread',
	'threadName']
	
log_format = lambda x: ['%({0:s})'.format(i) for i in x]
custom_format = ' '.join(log_format(supported_keys))

jslogger = logging.getLogger()
logHandler = logging.FileHandler('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/json-logfile.json')
formatter = jsonlogger.JsonFormatter(custom_format)
logHandler.setFormatter(formatter)
jslogger.setLevel(logging.DEBUG)
jslogger.addHandler(logHandler)


import logzero
from logzero import logger
from logzero import setup_logger

logzero.loglevel(logging.DEBUG)

logzero.logfile("/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/logfile.log", maxBytes=1e6)


loglogger = setup_logger(name="loglogger", logfile="/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/history-logfile.log", level=logging.DEBUG, maxBytes=1e6, backupCount=3, disableStderrLogger=True)

#jsonlogger = setup_logger(name="jsonlogger", logfile="/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/logs/rotating-logfile.json", level=logging.DEBUG, maxBytes=1e6, backupCount=3, disableStderrLogger=True,formatter=jsonlogger.JsonFormatter(custom_format))


#from collections import deque 
#queue = deque(["Ram", "Tarun", "Asif", "John"]) 
#print(queue) 
#queue.append("Akbar") 
#print(queue) 
#queue.append("Birbal") 
#print(queue) 
#print(queue.popleft())                  
#print(queue.popleft())                  
#print(queue)


import traceback
import inspect
#logger.info("E E 3 E")
#loglogger.debug("E E E 3 E E E")
#jsonlogger.debug("E E E E E E E")
#jslogger.debug('s',stack_info=True)
#jslogger.debug('e',exc_info=True)
#
#
#frame = inspect.currentframe()
#stack_trace = traceback.format_stack(frame)
#print(stack_trace[:-1])
#jslogger.debug(stack_trace[:-1])
#jslogger.debug("stack_trace", extra={'stack_trace' : stack_trace})


#logger.debug("Error Type: " + type(e))
#		logger.exception(e)
#		tb = sys.exc_info()[2]
#		logger.debug("Error: " + e.with_traceback(tb))


class Loge:
	def __init__(self, e):
		logger.debug("Error Type: " + str(type(e)))
		logger.exception(e)
		tb = sys.exc_info()[2]
		logger.debug("Error: " + str(e.with_traceback(tb)))
		
		
		loglogger.debug("Error Type: " + str(type(e)))
		loglogger.exception(e)
		loglogger.debug("Error: " + str(e.with_traceback(tb)))
		tbe = traceback.format_exc()
		tbs = traceback.format_stack()
		loglogger.debug("Exception Traceback")
		loglogger.debug(tbe)
		loglogger.debug("Exception Traceback")
		loglogger.debug("Stack Traceback")
		loglogger.debug(tbs)
		loglogger.debug("Stack Traceback")
		
		stack_trace = traceback.format_stack(inspect.currentframe())
		
		jslogger.exception(e)
		jslogger.debug("stack_trace", extra={'stack_trace' : stack_trace[:-1]})
		jslogger.debug("exc_info", exc_info=True)
		jslogger.debug("stack_info", stack_info=True)
	def __enter__(self):
		return self
	def __exit__(self, type, value, traceback):
		pass

