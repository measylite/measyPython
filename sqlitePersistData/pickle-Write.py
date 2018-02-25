# Measy Lite 2018. 
# Demo of objects - persist data to db

# Using sqlite w/ db-browser
# run on command line$ sqlite3
# .table 
# .header 
# .schema  
# .mode csv
# .mode insert 
# .mode list
# select x from 'table' limit 3
# .once optput.txt
# .select * from 'table'
# select max(colum) from 'table' where 'colum'= ddd
import sqlite3
import cPickle

#list of tules
def getStocks():
	stocklist = []
	conn = sqlite3.connect('/Users/measylite/code/remoteGit/measyPython/dbSqlite/scrapeSite.db')
	c = conn.cursor()
	c.execute('SELECT id, userCookie, catagory, content from instagram')
	for row in c.fetchall():
		stockTuple = (row[0], row[1],row[2],row[3])
		stocklist.append(stockTuple)
	return stocklist

#initialize list
stocklist=[]
stocklist = getStocks()
print len(stocklist)

#Pickle file
# r=read,w=write,rb=readBinary,wb=writeBinary
my_file = open("writenPickleBinary.dat" , "wb")
cPickle.dump(stocklist, my_file,2) #protocol version : 0-ascii, 1-binary or 2 binary
my_file.close()








