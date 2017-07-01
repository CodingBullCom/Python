#Write a short Python function, is_multiple(n, m), that takes 
#two integer values and returns True if n is a multiple of m, 
#that is, n = mi for some integer i, and False otherwise.

def is_multiple(n, m):
	return n%m == 0
	
print is_multiple(10, 2)
print is_multiple(10, 3)	
print is_multiple(104787388263762376487320, 2)
print is_multiple(104387463676573465786438, 3)