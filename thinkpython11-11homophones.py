#thinkpython 11.11 homophones

#Looks for words which are pronounced the same even when
#differing by one letter. (subtracting one letter from the first
# word)

import pronounce

def create_dict(filename):
	""" 
		filename: string

		Takes text file, creates a dict and returns it
	"""

	d = {}
	fin = open(filename)

	for line in fin:
		word = line.strip()
		d[word] = 0
	return d


def check_word(word,worddict,pronouncedict):
	""" Takes two words (s1 and s2) and checks to see if they have
		the same pronunciation. Compares in pronouncedict.

		pronouncedict is dictionary of pronounciations

		returns bool

		word: string
		worddict: dictionary
		pronouncedict: dictionary

	"""
	word1 = word[1:]
	word2 = word[0] + word[2:]
	if (word1 in pronouncedict) and (word2 in pronouncedict):
		if pronouncedict[word1] == pronouncedict[word2]:
			if (word1 in worddict) and (word2 in worddict):
				return True
	return False

if __name__ == '__main__':
	worddict = create_dict('words.txt')
	pronouncedict = pronounce.read_dictionary()
	
	for i in worddict:
		if check_word(i, worddict, pronouncedict) and (len(i) == 5):
			print i

#Changing the if statement to opposite would prevent me from
#having to nest. So, if not word in dict, return False.