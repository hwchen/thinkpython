#think python exercise 9.8
#Cartalk: reverse digit ages

#use zfill?
#Very interesting to see some of the answers. I should set a time
#to review answer to thinkpython

def reverse(x):
	"""
		Takes int, turns into string, then reverses,
		then returns int
	"""
	return int(str(x).zfill(2)[::-1])


def is_reverse(x,y):
	"""
		takes two integers, turns into string,
		and then compares to see if they are
		the reverse of each other
	"""

	x_string = str(x).zfill(2)
	y_string = str(y).zfill(2)
	reverse_y = y_string[::-1]
	if x_string == reverse_y:
		return True
	return False


def reversed_ages():
	"""
		seed starting at 1 through 9,
		then for each seed step through 2 loops to
		find the reverse age points. print out each set 

		If I want to find the set, I'd have to store it in
		a list or set a boolflag to find the first instance.
	"""

	total = 0
	for i in range (10):
		print 'seed: ' + str(i)
		j = reverse(i)
		while j <= 100:
			if is_reverse(i,j):
				print i, j
				total = total + 1
			i = i+1
			j = j+1	
		print 'total = ' + str(total)
		print''
		total = 0 #reset counter for next loop
reversed_ages()
