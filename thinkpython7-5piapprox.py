#factorial, pi approximation think python 7.5


import math

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def formula_numerator(n):
	return float((factorial(4*n) * (1103 + (26390 * n))))

def formula_denominator(n):
	return float(((factorial(n))**4) * (396 **(4*n)))
 
def front_of_formula():
	return 2 * math.sqrt(2) / 9801

def summation():
	n = 0
	temp_sum = 0
	summation = 0
	while True:
		temp_sum = float(formula_numerator(n))/formula_denominator(n)
		summation = summation + temp_sum
		n = n+1
		if temp_sum < 1e-15:
			break
	return summation
 
 
def pi_approx():
	return 1 / (front_of_formula() * summation())

print pi_approx()
print math.pi