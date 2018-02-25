# MeasyLite Python - 2018
# Set - add/discard, update, union/intersection, 
#  In or not in, unique membeship, unique no duplicate are stored.
#
# i.e s1 = set()
# 				s1.add(1)

watchList = ['zSFT', 'xPPL', 'yCOM']

#tuples
openPos = [('APPL',100.00,100), ('F',8.35,100), ('DIS',83.56,100)] #sym,buy,sell
closePos = [('MSFT',23.90,100), ('INTC',65.09,100), ('CSV',109.89,100)] #sym,buy,sell

myStocks = set()
for x in watchList:
	# myStocks.add(x[0])
	print "watchList: string char"
	print x[3]

for x in openPos:
	# myStocks.add(x[0])
	print x[0]

for x in closePos:
	# myStocks.add(x[0])
	print x[0]

print myStocks