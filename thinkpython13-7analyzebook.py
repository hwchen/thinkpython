#thinkpython13.7 
#Outputs a random word depending on its frequency in the book.
#Includes steps from previous problems, to process the book.
#I don't know if Downey's solution is correct. Because I'm
#not sure of his implementation of bisect and not moving
#the freqs over by one index. Double check later when
#have some more time to think about it.

#13.1, process text of a book.
#13.2 skip header of gutenberg book. process the rest of text

import string
import random

def open_book_to_list(filename, title):
	""" Opens text file, puts all words into a list 
		with no spaces, enlines, punctuation, uppercase.
		returns a list of words

	"""

	fin = open(filename)
	booktext = fin.read()

	header_end = booktext.rfind(title)
	booktext = booktext[header_end:]
	booktext = booktext.translate(None,string.punctuation)
	booktext = booktext.lower()
	return booktext.split()

def word_hist(t):
	"""Takes a list and creates a histogram.

		returns a dictionary """

	d = {}
	for word in t:
		d[word] = d.get(word,0) + 1

	return d


#13.4 Read a word list and compare the text to the word list.

def init_worddict(filename):
	"""Initializes the word list. returns a dictionary with 
		words as keys and mapping to 0

	"""

	d = {}
	
	fin = open(filename)
	for line in fin:
		word = line.strip()
		d[word] = 0

	return d


def compare_to_wordlist(bookdict, worddict):
	"""Takes the dictionary of words, checks to see if those words
		are in the worddict (a dict). Or actually, should be other
		way around. Prints the words that are not.

	"""

	for word in bookdict:
		if word not in worddict:
			print word

#13.5 random number from hist (dictionary mapping word to freq)

def choose_from_hist(d):
	"""given a dictionary histogram mapping words to frequency
		this function outputs a word with the probability related
		to the frequency of the word.

	"""
	t = [] #convert back to list?
	
	for word in d:
		for i in range(d[word]):
			t.append(word)

	randomindex = random.randint(0,len(t)-1)
	res = t[randomindex]
	return res

#13.7 add-ons

def bisect_insert(t, target):
	"""Takes a sorted list, bisect searches it. If not in list,
	returns the next index up for the base case. Returns index
	number. If no exact match and base case len == 1, will
	return the index that's closest above. Target must be
	in range of t."""
		
	midpoint = len(t)/2
	if t[midpoint] == target:
		return midpoint
	elif len(t) == 1:
		return 0
	elif t[midpoint] > target:
		return bisect_insert(t[:midpoint], target)
	elif t[midpoint] < target:
		return midpoint + bisect_insert(t[midpoint:], target)

def choose_from_hist2(d):
	"""given a dictionary histo mapping words to frequency
		This function outputs a word with the probability
		related to the frequency of the word.
		but uses a better algorithm. With this and 
		bisect insert, target will always slide
		to the left, but the indexes are off by one
		from the key list, so the hist amounts are correct"""
	
	t1 = d.keys()
	t2 = [0] #for hist, first value should be zero.
	total = 0
	for word in d:
		total += d[word]
		t2.append(total)

	#choose random int, find where it would slot into
	#the cumulative list t2, that index corresponds
	#to 
	target = random.randint(0,total-1)
	returnindex = bisect_insert(t2, target)
	
	#return the word
	return t1[returnindex]

if __name__ == '__main__':
	booklist = open_book_to_list('book.txt', "THE STUDENT'S")
	bookhist =  word_hist(booklist)
	worddict = init_worddict('words.txt')
	

	testhist = {"one":100, "two":100, "three":100}
	total = 0
	for i in range(100):
		result = choose_from_hist2(testhist)
		if result == "one":
			total += 1
	print total
