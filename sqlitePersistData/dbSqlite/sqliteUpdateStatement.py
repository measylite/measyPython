import sqlite3
from os import path

conn = sqlite3.connect("/Users/measylite/code/remoteGit/measyPython/scrapeSite.db")
c = conn.cursor()
x = 'money', 'insCookie',
c.execute('Update instagram set catagory=? where userCookie=?',x)
conn.commit()
conn.close()
print c.rowcount