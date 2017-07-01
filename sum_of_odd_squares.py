#Write a short Python function that takes a positive integer n and returns the 
#sum of the squares of all the odd positive integers smaller than n.

def sum_of_squares_of_odd_numbers(n):
	return (n*(2*n-1)*(2*n+1))/3
	
print sum_of_squares_of_odd_numbers(3)
print sum_of_squares_of_odd_numbers(5)
print sum_of_squares_of_odd_numbers(6)
print sum_of_squares_of_odd_numbers(7)