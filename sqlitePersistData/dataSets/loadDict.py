import csv

# Function
def getStockDict():
	dataFile = "companylist.csv"
	f = open(dataFile, "r")
	reader = csv.reader(f)
	myDict = {} #dictionary to hold sym&Name 
	for data in reader:
		myDict [data[0]] = data[1] # symbol, name, lastSale MarketCap, ADRTSO, IPOyear, sector, Industry, 
	# print len(myDict)
	# for x in myDict.keys():
	# 	print x, myDict[x]
	return myDict

print "\nCheck csv file for items, echo Error if not found: \n"
myDict = getStockDict()
mystocks = ['IBM','F','DISY']
for  x in mystocks:
	if x in myDict:
		print myDict[x]
	else:
		print "Error Not Found!"

