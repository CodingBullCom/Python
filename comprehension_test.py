#Give a single command that computes the sum of squares till a given number n,
#relying on Python's comprehension syntax and the built-in sum function

def sum_of_squares(n):
	return sum([x*x for x in range(n+1)])
	
print sum_of_squares(3)
print sum_of_squares(5)
print sum_of_squares(6)
print sum_of_squares(7)	
	