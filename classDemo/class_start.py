#
# Miguel Soria 
#

class myClass():
	def method1(self):
		print "myClass method1"

	def method2(self, someString):
		print "myClass method2 " + someString
		
# Inheritance demo another class based off myClass()
class anotherClass(myClass):
	def method2(self):
		print "anotherClass method2"
	
	def method1(self):
		myClass.method1(self);  # print myClas method1 
		print "anotherClass method1"
		

# main stub
def main():
	#demo instantiate or new up myClass()
	c = myClass()
	c.method1()
	c.method2("Hello Measy")

	#new up another class
	ac = anotherClass()
	ac.method1()
	ac.method2()
if __name__ == '__main__':
	main()