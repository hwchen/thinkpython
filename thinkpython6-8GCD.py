#Thinkpython exercise 6.8

#Greatest common denominator. Find the largest number that divides into both a and b 
#without remainder.

#simple algorithm: check each number up to b/2, then return the largest one.

#thinkpython algorithm: GCD of a and b is equal to GCD of b and a mod b

def gcd(a,b):

	#sort the numbers so a is bigger
	temp = 0
	if b > a:
		a = temp
		a = b
		b = temp

	# compare

	r = a % b
	if b == 1:
		return 1
	elif r == 0:
		return b
	return gcd(b,r)

print(gcd(24,9))