#think python exercise 10.3
#Takes a list of numbers. Returns a list of numbers
#with cummulative sum. e.g. [1,2,3] becomes [1,3,6]

def cummulative_sum(t):
	copy = []
	total = 0
	for i in t:
		copy.append(i+total)
		total += i
	return copy

t = [1,2,3,4,5,6,7,8,9]
print cummulative_sum(t)