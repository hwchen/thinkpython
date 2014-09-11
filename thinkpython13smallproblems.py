#Thinkpython Chapter 13 small problems (working with data)

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

#13.3, print 20 most frequently used words.

def twenty_most(d):
	"""Print twenty most used words. DSU pattern. Takes dictionary
		and converts to list of tuples, sorts, and prints"""
	t = []
	for word in d:
		t.append((d[word], word))

	t.sort(reverse = True)

	for x,y in t[:20]:
		print y

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

#13.6 set subtraction

def compare_to_wordlist2(bookdict, worddict):
	"""Takes dict of words, checks to see if those are in the word dict
		(also a dict). Uses set operations."""

	bookset = set(bookdict)
	wordset = set(worddict)

	res = bookset.difference(wordset)
	for i in res:
		print i

if __name__ == '__main__':
	booklist = open_book_to_list('book.txt', "THE STUDENT'S")
	bookhist =  word_hist(booklist)
	worddict = init_worddict('words.txt')
	#print 'total words = ' + str(len(booklist))
	#print 'number of different words = ' + str(len(bookhist))
	#print 'words in book but not in wordlist: '
	#print compare_to_wordlist(bookhist, worddict)
	#print choose_from_hist(bookhist)
	#twenty_most(bookhist)
	print 'words in book but not in wordlist: '
	print compare_to_wordlist2(bookhist, worddict)