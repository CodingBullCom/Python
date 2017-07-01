#Give a single command that computes the sum of the squares of all the odd positive integers
#smaller than n, relying on Python's comprehension syntax and the built-in sum function

def sum_of_squares_of_odd_numbers(n):
	return sum([x*x for x in range((n)*(n-1)) if x%2 != 0])
	
print sum_of_squares_of_odd_numbers(3)
print sum_of_squares_of_odd_numbers(5)
print sum_of_squares_of_odd_numbers(6)
print sum_of_squares_of_odd_numbers(7)	 