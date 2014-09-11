#Think Python chapter 9 small exercises

#9.1 read words.txt and prints only words with more
#more than 20 characters.

def more_than_twenty():
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word

#more_than_twenty()

#9.2, add has no e, print % of words in list 
#that don't have e

def has_no_e(word):
	"""
		Takes a string 'word', checks if letter 'e' is 
		in that word, and returns True if 'e' is not in
		the word.

	"""

	flag = True

	for letter in word:
		if letter == 'e':
			flag = False

	return flag

def list_no_e():
	"""Takes words.txt and checks to see
		how many words don't have an e. Sums
		the total of words and total of words
		without e, returns the percentage as a float.

	"""

	fin = open('words.txt')
	
	total_words = 0
	total_no_e = 0

	for line in fin:
		total_words = total_words + 1
		word = line.strip()
		if has_no_e(word):
			total_no_e = total_no_e + 1

	print 'words without e: ' + str(total_no_e)
	return float(total_no_e)/float(total_words)

#print '{0:.2f}'.format(list_no_e()) + ' %'

#9.3, function 'avoids' the given letter in a word. returns true if

def avoids(word, avoid_letters):
	"""
		Takes a string 'word', and then a string of letters. if the word 
		doesn't contain any of the letters in the string, then return True.
	"""
	flag = True

	for i in word:
		for j in avoid_letters:
			if i == j:
				flag = False
	return flag

#print avoids('hyperecstatic', 'hmul') 

def avoids_prompt():
	"""
		user enters string of forbidden letters into prompt.
		check list for words with those letters. Print the
		number of words that don't contain those letters
	"""

	avoid_letters = 'aeiou'#raw_prompt('enter forbiddent letters: ')

	total_avoiding_letters = 0

	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if avoids(word,avoid_letters):
			total_avoiding_letters = total_avoiding_letters + 1
	return total_avoiding_letters

#print avoids_prompt()

#exercise 9.4, function uses_only

def uses_only(word, uses_only_string):
	"""
		takes a word and a string, returns true if the word uses only 
		characters in the string.
	"""
	flag = True

	for i in word:
		if i not in uses_only_string:
			flag = False  
	return flag

#print uses_only('mulh', 'chmul') 

def uses_only_list():
	"""
		using word list, checks for words which only contain 'acefhlo'
		and prints each one
	"""

	uses_only_string = 'acefhlo'

	
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if uses_only(word,uses_only_string):
			print word
			
#print uses_only_list()

#Exercise 9.5, function uses all

def uses_all(word, uses_all_string):
	"""
		takes a word and a string, returns true if the word uses all 
		characters in the string at least once. (this one can use an and statement?)
		Actually, don't need and statement, just need to check from each char in 
		the string to the word, instead of from each char in the word to the string.
	"""
	flag = True

	for i in uses_all_string:
		if i not in word:
			flag = False  
	return flag

#print uses_all('mulchier', 'chmul') 

def uses_all_list():
	"""
		using word list, checks for words which uses the whole string 'aeiou'
		or aeiouy and prints each one and prints the total.
	"""

	uses_all_string = 'aeiouy'

	uses_all_total = 0

	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if uses_all(word,uses_all_string):
			print word
			uses_all_total = uses_all_total + 1
	return uses_all_total

#print uses_all_list()

#Exercise is_abecedarian

def is_abecedarian(word):
	"""Returns true if all the characters in the word are in alphabetical order

	"""
	flag = True
	
	for i in range(len(word)):
		if i == (len(word)-1):
			break
		elif ord(word[i+1]) < ord(word[i]):
			flag = False
	return flag 

#print is_abecedarian('abccdef')

def abecedarian_list():
	"""
		using word list, checks for words are abecedarian
		and prints each one and prints the total.
	"""

	abecedarian_total = 0

	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if is_abecedarian(word):
			print word
			abecedarian_total = abecedarian_total + 1
	return abecedarian_total

#print abecedarian_list()