import sqlite3
from os import path

conn = sqlite3.connect("/Users/measylite/code/remoteGit/measyPython/scrapeSite.db")

c = conn.cursor()

#select column form table
#c.execute('select userCookie  from users')

#select all columns from table
c.execute('select facebook, userCookie, catagory,content from users order by facebook')

#loop through our element
for row in c.fetchall():
	print row