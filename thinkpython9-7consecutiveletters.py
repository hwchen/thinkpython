#Thinkpython exercise 9.7
# find a word with three consecutive double letters

# give answer is a simpler while loop. My blind spot was resetting
#the counter back to one if there was a non-consecutive double.

def is_consecutive(string): #actually don't need this , number_consecutive_doubles is better
	""" Takes a string and determines if all
		characters are the same.

	"""

	first_letter = string[0]
	for letter in string:
		if letter != first_letter:
			return False
	return True

def number_consecutive_doubles(word):
	"""
		Recursive, returns the number of 
		consecutive doubles. base case 
		returns either 1 or 
		recursive part adds.
		Starts with the first letter.
	"""

	if len(word) < 2:
		return 0
	elif word[0] != word[1]:
		return 0
	return 1 + number_consecutive_doubles(word[2:])

#print number_consecutive_doubles('aaaaaaa')

def three_consecutive_doubles(word):
	"""Takes a word. Checks if it contains
		three consecutive doubles. If so,
		returns true. else false.

		Does this by checking slices. Should it 
		do this recursively? Yes, consecutive
		doubles should return 1. Or it should
		be a while loop. This would actually be
		simpler. Do both!

		first have to find the first consecutive
		sequence. then determine if there's 3.

	"""
	i = 0	#index for traversing word

	while i <= (len(word)-6): #prevent going over end of index.
		if number_consecutive_doubles(word[i:]) == 3: 
			return True
		i=i+1
	return False

#print three_consecutive_doubles('assdd;flkj;aldskkffjj')


def three_consecutive_doubles_list():
	"""
		Finds words with 3 consecutive doubles and prints and totals them
	"""
	total = 0

	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if three_consecutive_doubles(word):
			print word
			total = total + 1
	return total

print three_consecutive_doubles_list()

