class Dog:
	
	#speak method
	def speak(self):
		return "woof"
	def __str__(self):
		return "Dog"

# Concrete factory
class DogFactory:
	
	# return dog object 
	def get_pet(self):
		return Dog()

	# return dog food object
	def get_food(self):
		return "Dog Food!"

# petstore Abstract  Factory
class PetStore:
	
	# pet_factory is our Abstract Factory, 
	def __init__(self, pet_factory=None):
		
		#Store an instance of the concret factory class
		self._pet_factory = pet_factory

	# utility method display details return by the DogFactory
	def show_pet(self):
			pet = self._pet_factory.get_pet()
			pet_food = self._pet_factory.get_food()

			print("Our pet is '{}' !" .format(pet))
			print("Out pet says hello by '{}'".format(pet.speak()))
			print("Its food is '{}'".format(pet_food))

# Create a concrete Factory , Instantiate
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

#Invoke our util method to show details
shop.show_pet()
