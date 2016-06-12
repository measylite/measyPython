#
# Miguel Soria
#

# Builder patern
# director Abstract Builder: interfaces  | contrete builder inherit | product

class Director():
	# Director is the one building the car
	def __init__(self, builder):
		self._builder = builder

	def construct_car(self):
		# new car obj to get started
		self._builder.create_new_car()
		self._builder.add_model()
		self._builder.add_tires()
		self._builder.add_engine()
	
	def get_car(self):
		return self._builder.car
		
class Builder():
	#Abstract Builder
	def __init__(self):
		self.car = None

	def create_new_car(self):
		self.car = Car()

# Concrete builder provides parts and tools to work on the parts
class SkylarkBuilder(Builder):

	def add_model(self):
		self.car.model = "Skylark"

	def add_tires(self):
		self.car.tires = "Regular tires."

	def add_engine(self):
		self.car.engine = "Six cylinder engine"

# Car class
class Car():
	def __init__(self):
		self.model = None
		self.tires = None
		self.engine = None

	def __str__(self):
		return '{} | {} | {}'.format(self.model, self.tires, self.engine)

#create a contrete builder 
builder = SkylarkBuilder() #name of builder
director = Director(builder) #holding the director object (arg builder)
director.construct_car() # invoking the consturct car method
car = director.get_car() # director get a reference to the car object by invoking director gecar metod

print (car)

		
		