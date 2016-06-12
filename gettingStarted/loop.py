#
# Miguel Soria 
#

# Working with loops | Python only has two way of doing loops, while and for

# define a while loop
x = 0
while (x < 5):
	print x
	x = x + 1

# define a for loop notice we don't initialize z with.  for is an iterator
for z in range(5,10):
	print z

# iterate ovear a collection
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

for d in days:
	print d

# Break and Continue statement
for m in range(20,30):
	# if (m == 25): break #prints 20-24
	if (m % 2 == 0): continue #prints odd numbers 21-29 
	print m

# loop to print index and item, use enumberate
month = ["dum","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for i,d in enumerate(month):
	print i, d