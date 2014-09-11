#Thinkpython 13-8 Markov analysis.

import random
import string

def text_list(filename = 'emma.txt', title = 'VOLUME I', footer = 'FINIS'):
	"""Process text into a list"""
	t = []
	
	fin = open(filename)
	s = fin.read()
	header_end = s.rfind(title)
	footer = s.rfind(footer)

	s = s[header_end:footer]
	s = s.replace('-', ' ')
	s = s.translate(None,string.punctuation)
	s = s.lower()
	return s.split()
	

def markov(t, prefix_length):
	"""Takes a list that contains words from a text.
	Outputs a dictionary of tuples mapping each prefix to
	list of possible suffixes. Prefix length is int argument

	prefix_length: int
	t: list
	returns dict mapping tuples to lists"""

	d = {}
	for i in range(len(t) - prefix_length):
		prefix = ()
		for j in range(prefix_length):
			prefix += t[i+j],
		d.setdefault(prefix, []).append(t[i + prefix_length])

	return d

def generate_markov(d,n,prefix_length):
	"""Generates a sentence using the markov analysis. Length n
	d: dictionary mapping markov analysis
	n: int
	Shouldn't have to pass prefix_length. Future, check d for prefix?"""

	#initialize output
	t1 = []
	for prefix in d:
		t1.append(prefix)

	seed = random.choice(t1)
	t2 = []
	for i in range(prefix_length):
		t2.append(seed[i])

	print t2
	#continue markov could reconstruct prefix better?
	for j in range(n-prefix_length):
		prefix = ()
		for k in range(prefix_length):
			prefix += t2[j+k],
		t2.append(random.choice(d[prefix]))
	return string.join(t2, ' ')
		
			

if __name__ == '__main__':
	t = text_list()
	d = markov(t,2)
	print generate_markov(d,500,2)
