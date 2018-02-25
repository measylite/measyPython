# MeasyPython
# To Open read and parce comma seperated values.


maxValue = 0.0 # Max vaule of stock this year
with open('CSV.csv', 'r') as f:
	first = f.readline()
	for line in f:
		#split on ,
		splitline = line.split(",")
		#closing price 4th position
		if float(splitline[4]) > maxValue:
			maxValue = float(splitline[4])
		#print line
f.close()
print maxValue