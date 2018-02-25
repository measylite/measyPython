import sqlite3
from os import path

conn = sqlite3.connect("/Users/measylite/code/remoteGit/measyPython/scrapeSite.db")

c = conn.cursor()

#select column form table
#c.execute('select userCookie  from users')

#select multiple argument to the table
# x = 'erotica','anchorTags'
# c.execute('select facebook, userCookie, catagory,content from users where catagory=? or catagory=?',x)

#get num row in table instagram 
c.execute('SELECT count(catagory) FROM instagram')

#loop through our element
for row in c.fetchall():
	#return mutiple selection
	# print row[0],row[1],row[2],row[3] 
	print row[0]