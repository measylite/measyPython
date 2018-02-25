import csv

dataFile = "companylist.csv"
f = open(dataFile, "r")
reader = csv.reader(f)
count = 0 #Limit number
for data in reader:
	print data[0], data[1]
	count = count + 1
	if count > 6:
		break