import sqlite3
from os import path

conn = sqlite3.connect("/Users/measylite/code/remoteGit/measyPython/scrapeSite.db")

c = conn.cursor()
#select multiple argument to the table
x = 9087979,'uemailIinsCookie','comedy','get quoates'
c.execute('Insert into instagram values(?,?,?,?)' , x)
conn.commit()
conn.close()
print c.rowcount