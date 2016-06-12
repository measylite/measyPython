#
# Miguel Soria
#

# Imports  
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
	print os.name; # posix

	# check for the item existance and type
	print "File or Item exists: " + str(path.exists("textfile.txt"))
	print "File Item is a file: " + str(path.isfile("textfile.txt"))
	print "Item is a directory: " + str(path.isdir("textfile.txt"))

	# file path manipulation
	print "File or Items path: " + str(path.realpath("textfile.txt"))
	print "File or Items path, name has been split out; " + str(path.split(path.realpath("textfile.txt")))

	# get file modificaion time dont forget your class imports
	t = time.ctime(path.getmtime("textfile.txt"))
	print "Last modificaion time: "+ t

	#date time format rather than a c time format
	# print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print "Last modificaion date object: " + str(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) 

	# Date calculation to see how long ago a file was modified
	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print "It has been " + str(td) + " since this file was edited"
	print str(td.total_seconds()) + " <-- Seconds"

if __name__ == '__main__':
	main()