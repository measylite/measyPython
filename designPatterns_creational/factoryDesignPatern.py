#
# Miguel Soria
#

class Dog:
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof"

# New Class Object add cat
class Cat:
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow"

# Get PET Method 
def get_pet(pet="dog"):
	#factory method
	pets = dict(dog=Dog("Lucius"), cat=Cat("Coco"))
	return pets[pet]



	# This is pythons implementation os the factory patern
	# 	We are adding new classes aka pet dog cat fish etc
	# 	We use the get_pet() mehtod to call the speak method 
	# 	get_pet() uses a dictionationary to hold our object with a key value pair.  

d = get_pet("dog")
print d.speak()

c = get_pet("cat")
print c.speak()
