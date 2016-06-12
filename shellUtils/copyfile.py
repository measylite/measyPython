#
# Miguel Soria
#

# shell utilities copy and make a backup of a file

import os
import shutil
from os import path

def main():
	#make a duplicate of already existing file
	if path.exists("textfile.txt"):
		# get path in current dir
		src = path.realpath("textfile.txt");

	# Strip the path from the file name
	head, tail = path.split(src)
	print "path: " + head
	print "file: " + tail

	# duplicate it and rename
	dup = src + ".bak"
	# use shell util to mak the copy of the file
	shutil.copy(src,dup)

	# use this shell util if we need meta data, permission, timstamp, etc 
	shutil.copystat(src,dup)


if __name__ == '__main__':
	main()