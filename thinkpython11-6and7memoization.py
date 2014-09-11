#thinkpython 11.6 and 11.7, memoization

#11.6, fibonacci memoization
import time

def fib(n):
	known = {0:0, 1:1}
	if n in known:
		return known[n]
	
	result = fib(n-1) + fib(n-2)
	known[n] = result
	return result


def fib_old(n):
	if n == 0:
		return 0
	if n ==1:
		return 1
	return fib(n-1) + fib(n-2)

#stime = time.time()
#print fib(35)
#ftime = time.time()
#print 'time elapsed: ' + str(ftime - stime)

#stime = time.time()
#print fib_old(35)
#ftime = time.time()
#print 'time elapsed: ' + str(ftime - stime)

#11.7 Memoize Ackermann

# A(m,n)
# if m = 0, n+1
# if m>0 and n=0, call A(m-1,1)
# if m>0 and n>0, call A(m-1, (A(m,n-1)))
#solution uses tuples. Also, can only do the last case,
#it's the true recursive case, other two are not complete (base)
#and he uses try/ before explaining it in the book. (and tuples)
#dicts in dicts is too confusing.

def ack(m,n):
	known = {}
	if (m,n) in known:
		return known[m,n]
	elif m == 0:
		temp1 = n+1
		known[m,n] = temp1
		return temp1
	elif m > 0 and n == 0:
		temp2 = ack(m-1,1)
		known[m,n] = temp2
		return temp2
	elif m > 0 and n > 0:
		temp3 =  ack(m-1, ack(m,n-1))
		known[m,n] = temp3
		return temp3

print(ack(3,7))
