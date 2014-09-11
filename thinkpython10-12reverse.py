#Think python 10.12
#Two words are a reverse pair if one is the reverse of the other.
#for example, "ton" and "not". Find all reverse pairs in word list
#I'm using 2 for loops. There must be a faster way.
#Ah, the faster way is to simply reverse the word and then search
#for it using bisect.


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

#bisect search from 10-11

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

def reverse_string(s):
	"""Takes a string, reverses and returns the reverse
	"""
	return s[::-1]

def search_reverse(t):
	""" looks through list of sorted words using bisect search.
		For each word, reverses it, and then searches
		for the reverse. only need to search n/2 of the list

	"""
	for i in t:
		s = i[::-1]
		reverse_index = bisect(t,s)
		if reverse_index != None:
			print 'reverse pair: '+str(i)+', '+str(t[reverse_index]) 

t = list_generator('words.txt')
search_reverse(t)