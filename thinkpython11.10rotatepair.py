#Think Python exercise 11.10 rotate pairs
#Find all of the words that you can rotate (using wordlist)
#rotating is moving all the letters in a word up by a certain
#number

def rotate_word(s, n):
	""" Takes a string, rotates it by n letters up.

		s: string
		n: integer
		returns: a string

	"""
	copy = ''
	for letter in s:
		ordinal = ord(letter) - ord('a')
		#print ordinal, letter
		rotated_ordinal = (ordinal + n)%26
		rotated_letter = chr(ord('a') + rotated_ordinal)
		#print rotated_ordinal, rotated_letter
		copy = copy + str(rotated_letter)

	return copy

#print rotate_word('xyz', 1)

def is_rotated(filename, n):
	"""	Finds all of the word pairs that are rotated
		using one dictionary.

		convert word list to dictionary. if rotated in
		dictionary, print.

		n: integer, is the number to rotate by

	"""
	d = {}
	fin = open(filename)

	for line in fin:
		word = line.strip()
		d[word] = 0

	for i in d:
		rotatedword = rotate_word(i,n)
		if rotatedword in d:
			print i, rotatedword

for i in range (1,13):
	is_rotated('words.txt', i)