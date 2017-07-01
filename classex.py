class MyClass:
	"""A simple example class"""
	i = 12345
	def say_hello(self, name):
		return "Hello! " +name

x = MyClass()
print x.say_hello("Python") 