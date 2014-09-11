#thinkpython 10.13
#interlocking words

#finding two words which, when interlocked, create a third

#first, add list generator and bisect search from previous problems

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

#interlock two words

def interlock(s1,s2):
	"""Takes two strings. Since it's one addition at a time,
		need lists.
	"""
	t1 = list(s1)
	t2 = list(s2)
	copy = ''

	i = 0
	j = 0

	while (i < len(s1)) and (j < len(s2)):
		copy = copy + s1[i] #can also use lists, then join str
		copy = copy + s2[j]
		i += 1
		j += 1
	return copy

#test
#print interlock('shoe', 'cold')

def uninterlock(s):
	""" Takes a string and uninterlocks it, returns a list
		of 2 strings.
	"""

	i= 0
	copy = ['','']
	
	while i < len(s)-1:
		copy[0] += s[i]
		copy[1] += s[i+1]
		i+=2
	
	#to account for odd numbers
	if len(s)%2 != 0:
		copy[0] += s[len(s)-1]

	return copy
#test uninterlock
#print uninterlock2('schooled')

#the interlock search

def interlock_search(t):
	""" takes a list, checks for all words which are interlocks
		Does this by taking a pair of words, interlocking, then
		checking if the interlock is also in the word list.
		Whoops, should do opposite. Take a word and uninterlock
		it, and bisect search for the resulting two words.

	"""

	for i in t:
		uninterlocked = uninterlock(i)
		uninterlocked_1 = bisect(t,uninterlocked[0])
		uninterlocked_2 = bisect(t,uninterlocked[1])
		if (uninterlocked_1 != None) and (uninterlocked_2 != None):
			print t[uninterlocked_1]+' and '+t[uninterlocked_2]
			print 'become: ' + i
			print''

#t =  list_generator('words.txt')
#interlock_search(t)

"""
	For interlocking 3!
"""
def uninterlock3(s):
	""" Takes a string and uninterlocks it by 3, returns a list
		of 3 strings.
	"""

	i= 0
	copy = ['','','']
	
	while i < len(s)-2:
		copy[0] += s[i]
		copy[1] += s[i+1]
		copy[2] += s[i+2]
		i+=3
	
	#to account for non-mulitple of 3
	if len(s)%3 != 0:
		copy[0] += s[len(s)-2]
		copy[1] += s[len(s)-1]

	return copy
#test uninterlock
#print uninterlock3('schooled')

def interlock_search3(t):
	""" takes a list, checks for all words which are 3-interlocks
		Take a word and uninterlock	it, and bisect search for 
		the resulting 3 words.

	"""

	for i in t:
		uninterlocked = uninterlock3(i)
		uninterlocked_1 = bisect(t,uninterlocked[0])
		uninterlocked_2 = bisect(t,uninterlocked[1])
		uninterlocked_3 = bisect(t,uninterlocked[2])
		if (uninterlocked_1 != None) and (uninterlocked_2 != None) and (uninterlocked_3 != None):
			print t[uninterlocked_1]+' and '+t[uninterlocked_2]+' and '+t[uninterlocked_3]
			print 'become: ' + i
			print''

t =  list_generator('words.txt')
interlock_search3(t)

#In solution, he doesn't pass the list. He checks
#if the word can be interlocked in the first function
#so only has to pass a bool. This should be less expensive
#also, forgot about string [::2]