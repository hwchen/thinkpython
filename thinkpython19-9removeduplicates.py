#Thinkpython exercise 10.9
#remove_duplicates

"""
Takes a list, returns a new list with only unique elements

"""

def has_duplicates(letter,t):
	""" checks for duplicate if a letter
		 in a list by checking if it appears twice.
		modified From exercise 10-8.
	"""
	total = 0
	for i in range(len(t)):
		if letter == t[i]:   
			total += 1			
	if total > 1:
		return True

def remove_duplicates(t):
	"""

	"""
	copy = []
	for i in t:
		if not has_duplicates(i,t):
			copy.append(i)

	return copy

t = [1,2,3,4,5,6,7,8,9,9, 5,0,6]

print remove_duplicates(t)
