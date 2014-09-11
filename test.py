#testing for passing arguments into functions

#Pass a list in.

def test1(t):
    a = t
    a.append('test')

#testlist = [1,3,5]
#test1(testlist)
#print testlist


#Pass a primitive in.
#You can't modify a primitive? Is what happens
#That a new primitive assignment is actually
#a new object? Is that what they mean by immutable?

def test2(i):
    x = i
    x = 3
    return x

#testx = 5
#print test2(testx)
#print testx

#testing for list concatenation

#t = [1,2,3]
#x = t + [4]
#print x
#print t

cache = {}

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        
        return cache[m, n]

print ackermann(3, 4)
print ackermann(3,6)