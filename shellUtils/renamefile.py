#
# Miguel Soria
#

# Lets rename a file textfile.txt.bak does not exist runn copyfile.py to create it 
import os
import shutil
from os import path

def main():
	if path.exists("textfile.txt.bak"):
		src = path.realpath("textfile.txt.bak");

		os.rename("textfile.txt.bak", "renamed_file.txt")

if __name__ == '__main__':
	main()