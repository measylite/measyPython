import sqlite3
from os import path

conn = sqlite3.connect("/Users/measylite/code/remoteGit/measyPython/scrapeSite.db")
c = conn.cursor()
#update param is the fist   
x = 'testDelete',
c.execute('Delete from instagram where userCookie=?',x)
conn.commit()
conn.close()
print c.rowcount