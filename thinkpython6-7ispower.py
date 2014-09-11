#Think Python exercise 6.7

#is_power takes two numbers and returns True if a is a power of b

def is_power(a,b):
	if a / b == 1:
		return True
	elif a%b != 0:
		return False 
	return is_power(a/b, b)

print is_power(64,2)