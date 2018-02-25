import urllib2

# https://finance.yahoo.com/quote/F/history?ltr=1

# with open('mystocs.cvs') as f:
# 	for stk in ['AAPL', 'F']:
# 		url = "https://finance.yahoo.com/quote/F/history?ltr=1"
# 		pass


url = "https://finance.yahoo.com/quote/F/history?ltr=1"
sourceCode = urllib2.urlopen(url).read()
# splitSource = sourceCode.split('\n')
# for eachLine in splitSource:
# 	spl
# 	pass


#data Strucutes

# [] list collections of items, membership in or not in, append , insert , pop, sort.
# {} dictionaris - key value pair
# () tuples - join data, can couple with dictionary, immutable cant add or suptract model a record ()
# set() Union and Intersection with sets, unique membership (watchlist)





# maxValue = 0.0 # Max vaule of stock this year
# with open('CSV.csv', 'r') as f:
# 	first = f.readline()
# 	for line in f:
# 		#split on ,
# 		splitline = line.split(",")
# 		#closing price 4th position
# 		if float(splitline[4]) > maxValue:
# 			maxValue = float(splitline[4])
# 		#print line
# f.close()
# print maxValue