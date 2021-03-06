#
# Miguel Soria
#

# Prototype, clone an object and store in a dict 
import copy


class Prototype:

	def __init__(self):
		# initilize a dict to hold our kev value objs
		self._objects = {}
		
	def register_object(self, name, obj):
		#register obj
		self._objects[name] = obj

	def unregister_object(self, name):
		#remove obj
		del self._objects[name]

	def clone(self, name, **attr):
		#clone obj 
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(attr)
		return obj

class Car:
	def __init__(self):
		self.name = "Chevy"
		self.color = "Black and Yellow"
		self.options = "Fully Loaded"

	def __str__(self):
		return '{} | {} | {}'.format(self.name, self.color, self.options)

# Let see it clone a Car class 
c = Car()
prototype = Prototype()

# prototype.register_object('Camaro', c)
prototype.register_object('Camaro',c)
c1 = prototype.clone('Camaro')

print c1