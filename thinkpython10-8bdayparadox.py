#thinkpython exercise 10.8
#birthday paradox

"""
Generating a list inside of another function seems bad.
Better to generate to global and that pass that?
Or at least to destroy.

If I had to design more abstractly, I think that the
encapsulation would be better too.
"""

#part one: has_duplicates takes a list, then returns True if any
#letters in it are duplicated. Don't modify the original list.

import random

def has_duplicates(t):
	""" Makes a duplicate of original list and
		 see if it containes duplicates of any letter.

	"""
	#make copy
	for i in range(len(t)-1):
		if t[i] in t[i+1:]:   #does this create new lists? maybe
			return True			#not very efficient.
	return False

#t = [1,2,3]
#print has_duplicates(t)

#part 2: what is the probability that 2 students in a class of 23
#have the same birthday. seed with randint function

def generate_sample(x,y):
	""" generates a list of y samples. each sample is a list of 
		x integers. Is this an appropriate list generator?
		Or should I pass in an initialized list?

		it's a list of birthdays, so constrained by 365 days.

	"""
	samplegroup = []
	for i in range(y):
		temp = []
		for j in range (x):
			temp.append(random.randint(1,365))
		samplegroup.append(temp)
	return samplegroup

def same_bday():
	""" estimating probility by generating random birthdays
		and seeing how many of them are duplicates.
		Calls generate_sample, which creates a list of 
		lists (sample groups)

	"""
	totalmatch = 0
	numbersamples = 1000
	samplelength = 23

	#initialize samples

	sample = generate_sample(samplelength, numbersamples)

	#test for matches
	for x in range(numbersamples):
		if has_duplicates(sample[x]):
			totalmatch+=1

	#calculate the probability

	return totalmatch/float(numbersamples)
	
#print generate_sample(23,100)
print same_bday()

