#
# Miguel SOria
#

# Working with conditional statements if(<) else(>) elif(=) 
def main():
	x, y = 1000, 1000
	
	if(x < y):
		stmt = "X is less than Y"
	elif(x == y):
		stmt = "X is equal to Y"
	else:
		stmt = "X is greater than Y"
	print stmt

if __name__ == '__main__':
	main()
