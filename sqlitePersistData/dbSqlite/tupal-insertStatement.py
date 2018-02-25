import sqlite3
from os import path

conn = sqlite3.connect("/Users/measylite/code/remoteGit/measyPython/scrapeSite.db")
c = conn.cursor()
#update param is the fist   
content = [(234345, 'snapFish2','fishing2','alot of nothing2'),
		   (343633, 'farmAnimal2','dateAfarmer2','simple pig stuff2'),
		   (345633, 'scrapeSite2','smartData2','ssh this is a special2'),]
c.executemany('INSERT into instagram values(?,?,?,?)',content)
conn.commit()
conn.close()
print c.rowcount