from random import randint

class Die():
	'''a class represents die'''
	
	def __init__(self, num_sides=6):
		'''die has six sides'''
		self.num_sides = num_sides
		
	def roll(self):
		'''return a random value between 1 to 6'''
		return randint(1, self.num_sides)
