
#exercise 11.1: storing wordlist as keys in a dictionary.

import time

def word_key(f):
	"""
		Takes words.txt and reads each word into a key of
		a dictionary, which gets returned.
		f: string name for a file
	"""
	d = {}
	fin = open(f)
	for line in fin:
		word = line.strip()
		d[word] = 0
	return d

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


#d = word_key('words.txt')	#initial hash longer, search faster
#stime = time.time()
#print 'zephyr' in d
#ftime = time.time()
#print ftime - stime


#t = list_generator('words.txt')
#stime2 = time.time()
#print 'zephyr' in t
#ftime2 = time.time()
#print ftime2 - stime2

#Exercise 11.2- histogram with get

def histogram1(s):
	"""	takes a string and counts the instances of each letter.
		returns as a dict with key = letter and value = count.

		s: string
	"""
	d = {}
	for i in s:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	return d

def histogram2(s):
	d = {}
	for i in s:
		d[i] = d.get(i,0) + 1
	return d

#print histogram2('bubble')

#thinkpython 11.3: use keys to modify print_histogram to alpha order
#need to print both keys and values in alpha order, using
#a transfer of the keys to a list?
#I'm just using Python's sort. Kind of feels like cheating...

def print_h(h):
	for c in h:
		print c, h[c]

def print_h_alpha(h):
	t = h.keys()
	t.sort()
	for i in t:
		print i, h[i]


#h = histogram2('parrot')
#print_h_alpha(h)

#Exercise 11.4 reverse lookup, modify reverse lookup to
#build and return a list of all keys that map to v, or
#an empty list if there are none.

#dictionaries are setup up to search by key, so reverse
#lookup is much slower.

def reverse_lookup(d,v):
	"""	d: dictionary
		v: value (the target)

		given a dictionary and a dictionary value,
		looks up the key. (this means that a value)
		may have multiple keys). this version finds
		only the first key.
	"""
	for i in d:
		if v == d[i]:
			return i
	raise ValueError

def reverse_lookup_all(d,v):
	"""Modifies to include all keys of a value, returns
		list or empty list
	"""
	t = []
	for i in d:
		if v == d[i]:
			t.append(i)
	return t

#d = histogram2('alabaster')
#print reverse_lookup_all(d,3)

#11.5 invert dictionary, then modify it to have it work 
#with .setdefault

def invert_dict(d):
	""" Takes a dictionary, inverts values and keys
		(if there are multiple keys for a value)
		in the first dict, then those keys become a
		list of values in the second dict.
	"""
	copy = {}
	
	for k in d:
		if d[k] not in copy:
			copy[d[k]] = [k]
		else:
			copy[d[k]].append(k)
	return copy

def invert_dict2(d):
	"""using setdefault"""
	copy = {}
	for k in d:
		copy.setdefault(d[k],[]).append(k)
	return copy

#Fewer times accessing list is better. ?
#setdefault returns the value associated
#with the key, which then can be appended to.
#get returns default, but won't put it into the
#dictionary automatically.
#stackoverflow says .get has fewer side effects?
d = histogram2('alabaster')
print invert_dict2(d)

