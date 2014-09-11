#think python exercise

#capitalize list of nested lists of strings

def capitalize_all(t):
	"""	takes a list of strings and capitalizes all characters in it. returns a 
		copy of the list with each string capitalized.

	"""
	copy = []
	for i in t:
		if type(i) == str:
			copy.append(i.capitalize())
		else:
			copy.append(capitalize_all(i))
	return copy
t = [['asdfsa', ['qoewiurp', 'qpeofij']], 'z,mcmz']
print capitalize_all(t)
