#
# Miguel Soria
#

# Singleon Patern  Borg design patern make the class atribue global
# Only Instantiat e Once

class Borg:
		
		# Attribute Dictionary
		_shared_state = {}

		def __init__(self):
			# make it an attribute dict
			self.__dict__= self._shared_state	
			
# Inherit from the Borg Class
class Singleon(Borg):
	
	# This class shares all it attributes among its instances
	def __init__(self, **kwargs):
		Borg.__init__(self)
			
		# update dict by inserting key value pairs
		self._shared_state.update(kwargs) 
		
	# Return attribute dict
	def __str__(self):
		return str(self._shared_state)
		


# Create a singleton object
x = Singleon(HTTP = "Hyper Text Transport Portocol")

# Print obj
print x 

# Create another singleton object
y = Singleon(URL = "Universal Resource Locator")

# print other obj
print y

# add yet another 
z = Singleon(FTP = "File Transport Portocol")
print z 		
				
