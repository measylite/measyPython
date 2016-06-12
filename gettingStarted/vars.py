#
# Measy Demo Python - Let get it popin pimpin
#

# Vars
f =0;
print f 

# var redeclare
f = "abc"
print f

# type can not be combined, Strongly typed language 
print "String" + str(123) # we must cast


#------------ Global vs Local Variable 
g = 1 #local
print g

def someFunction():      # Define a function
	global g
	g = "Measy is a G!"
	print g

someFunction()  # If I dont set global in somefunction then I will lose the copy of var g = 1

print g

#-------------------Delete function
h = "GetPaidOrDieTrying"
print h 

del f 
print f   # will produce error message var f is gone.