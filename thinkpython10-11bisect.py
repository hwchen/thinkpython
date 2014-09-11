#thinkpython 10.11 bisect

#Takes sorted list and target value, searches by bisecting list
#and determining which side to search on. Recursive.

#generate list

def list_generator(filename):
	""" Takes a string (name of file) and returns
		a list made with each element as a line 
		from the file

	"""
	t = []

	fin = open(filename)
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

#bisect search

def bisect(t, target):
	"""
		bisect search takes a sorted list, and searches by 
		determining	whether the target is to right or left
		of the bisection point.
	"""
	bisector = (len(t)/2)		#this will round it down for odd#s
	
	if target == t[bisector]:
		return bisector
	elif len(t) == 1:
		return None
	elif target < t[bisector]:	#left 1st, cause of bisect rounding?
		#print t[:bisector] for debug!
		return bisect(t[:bisector], target)
	elif target > t[bisector]:
		#print t[bisector:] for debug!
		temp = bisect(t[bisector:], target)
		if temp == None:		#need to pass only None
			return None
		return temp + bisector
				#when going to right, need to add index
#t = list_generator('words.txt')
#target = 'ant'

#for debug, figured out need to add index to right
t = [1,3,5,7,9,11,13,15,17,19]
target = 17



targetindex = bisect(t,target)
print 'target is ' + str(target)
if targetindex == None:
	print 'Not in List'
else:
	print 'index is ' + str(targetindex)
	print 'result is ' + str(t[targetindex])

#Oops, doesn't behave properly if there is no match! Need to figure out how to propagate "none"
#up the chain.

# Easiest way to fix is to make bisect t/f, then a wrapper function
#that finds the given element in the list 