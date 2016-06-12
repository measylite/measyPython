#
# Miguel Soria
#

# Fetching internet data

import urllib2

def main():
	# open connecton to a url
	earl = urllib2.urlopen("http://www.brooklyncorners.com")

	# http connection response  200 
	print "Connection status: " + str(earl.getcode())

	# read dat from url and print it
	data = earl.read()
	print data

	
if __name__ == '__main__':
	main()