#Python's random module includes a function choice(data) that returns a random element
#from a non-empty sequence. The random module includes a more basic function randrange,
#with parameterisation similar to the built-in range function, that return a random
#choice from the given range. Using only the randrange function, implement your own
#version of the choice function.

import random

def choice(data):
	return data[random.randrange(len(data))]
	
print choice([10, 20, 30, 40, 50, 60, 70, 80, 90])
print choice([17, 22, 35, 46, 51, 63, 79, 84, 97])	
	