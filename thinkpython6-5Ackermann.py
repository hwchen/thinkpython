#Ackermann, exercise 6.6 Think Python

# A(m,n)
# if m = 0, n+1
# if m>0 and n=0, call A(m-1,1)
# if m>0 and n>0, call A(m-1, (A(m,n-1)))

def ack(m,n):
	if m == 0:
		return n+1
	elif m > 0 and n == 0:
		return ack(m-1,1)
	elif m > 0 and n > 0:
		return ack(m-1, ack(m,n-1))

print(ack(3,7))
