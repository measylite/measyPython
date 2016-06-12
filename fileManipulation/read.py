#
# Miguel Soria
#

def main():
	f = open("textfile.txt","r")

	# This way dumps the entire file out 
	# if f.mode == 'r':
	# 	content = f.read()
	# 	print content

	# This we read each individual line into a list using readlines()
	rl = f.readlines()
	for x in rl:
		print x


if __name__ == '__main__':
	main()