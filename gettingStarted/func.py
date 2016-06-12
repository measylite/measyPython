#
# Measy and python  
#

def myfunction():
	print "myfunction"

myfunction()
print myfunction() # tries to print the ruturn value
print myfunction   # function are objects value of myfunction object


#----- function with args
def funcWithArgs(arg1, arg2):
	print arg1, " ", arg2

funcWithArgs(10,20)
funcWithArgs("yo","momma")
print funcWithArgs("yo","momma") # no reutn 

#---------------------function with ruturn 
def cube(x):
	return x*x*x	

print cube(3)		


#--------------------------function with a default value if none given.  x=1
def power(num, x=1):
			result = 1
			for x in range(x):
				result = result * num
			return result

print power(2)
print power(2,3) 
print power(x=3, num=2)		# Reversed order, called by their name  8


#---------------------------function with unlimited args
def multi_add(*args):
	result = 0
	for x in args:
		result = result + x
	return result

print "Multi argument function"
print multi_add(2,4,8,0,2,3)
