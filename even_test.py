#Write a short Python function, is_even(k), that takes an integer value and 
#returns True if k is even, and False otherwise. However, your function cannot
#use the multiplication, modulo, or division operators.

def is_even(k):
	return k&1 == 0
	
print is_even(2)	
print is_even(3)
print is_even(234883897287223678623786)
print is_even(234883897287223678623781)