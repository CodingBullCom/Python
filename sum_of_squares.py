#Write a short Python function that takes a positive integer n and returns 
#the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
	return (n*(n+1)*(2*n+1))/6
	
print sum_of_squares(3)
print sum_of_squares(5)
print sum_of_squares(6)
print sum_of_squares(7)