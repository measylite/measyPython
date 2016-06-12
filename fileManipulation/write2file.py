#
# Miguel Soria 
#

#Read and Write files using built in Python file methods

def main():
	# Open a file for writing, create it if it doesn't exist => +
	# f = open("textfile.txt", "w+") # write
	f = open("textfile.txt", "a+") # append
	
	# Lets write something 
	for i in range(20):
		f.write("This is my line number %d\r\n" % (i+1))

	# Close file 
	f.close()

if __name__ == '__main__':
	main()