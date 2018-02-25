import cPickle

# r = read, w = write, rb = readBinary, wb = writeBinary
# r/w: 0-ascii, rb/wb: 1-binary or 2 binary

my_file = open("writePickle.dat", "rb")
myPickleList = cPickle.load(my_file)
for x in myPickleList:
	print x[1],x[2]
