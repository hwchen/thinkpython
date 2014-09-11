# Think Python Exercise 8.1

# program takes a string, displays each letter from back to front, one letter per line.

def word_backwards(user_string):
	"""

	"""
	for i in range(len(user_string)):
		print user_string[len(user_string)-1 - i]

#word_backwards('left')

def ducks():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'

	for letter in prefixes:
		if letter == 'O' or letter == 'Q':
			print letter + "u" + suffix
		else:
			print letter + suffix

ducks()

#fruit = 'banana'
#print fruit[:]

def find(word, letter, start_index):
	index = start_index
	while index<len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

#print find('a;sdlkjrghasl;dkh', 'r', 8)

def count1(word, letter):
	sum = 0
	for i in word:
		if i == letter:
			sum = sum + 1
	return sum

#print count1('hippo', 'i')

def count2(word, letter):
	sum = 0
	index = 0
	while True:
		if find(word, letter, index) == -1:
			break
		sum = sum + 1
		index = find(word, letter, index) + 1
	return sum

#print find('hippolllyte', 'l', 7)
#print count2('hippolllllllllyte', 'l')

#fruit = 'banana'
#print fruit.count('a')
