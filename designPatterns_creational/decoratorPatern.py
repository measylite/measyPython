#
# Miguel Soria
#

#imports
from functools import wraps


#Define Decorator
def make_blink(function):
	@wraps(function) 

	def decorator():
		#grab and return val os func being decorated
		ret = function()

		#add new functionality, decorate
		return "<blink>" + ret + "</blink>"
	# 	
	return decorator


# apply decorator
@make_blink

def hello_world():
	
	"""MeasyOne Kinobey"""
	return "Basic Bitch"


# When using he decorator pattern make sure you import you class
# create a function (def) | use @wrap
# use the decorator your other functions by alling the decorator 

# calling decorator result@makeblink  
print hello_world()
# check if function name is still the same after decorations
print hello_world.__name__
# check if docstring name is still the same after decorations
print(hello_world.__doc__)