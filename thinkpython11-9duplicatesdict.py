#thinkpython 11.9 has_duplicates in dict

def has_duplicate(t):
	""" Takes a list, converts to dictionary, checks if an object 
		appears more than once.

		The dictionary uses setdefault to count instances
		of a letter

		t: list

	"""

	d = {}
	for i in t:
		d[i] = d.get(i,0) + 1

	for k in d:
		if d[k] > 1:
			return True
	return False



# The faster version checks the list directly against the 
# dictionary. The dictionary is hashed, so checks directly,
#Don't have to iterate to it. And breaks out if if the list
#value is present in the dictionary key.

def has_duplicate_soln(t):
	d = {}
	for i in t:
		if i in d:
			return True
		d[i] = 0	#I don't think it matters the value here.
	return False

t = [1,2,3,4]

print has_duplicate_soln(t)

