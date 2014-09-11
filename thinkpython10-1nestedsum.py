#thinkpython exercise 10.1
#nested sum
#write a function that sums nested lists of integers.

def nested_sum1(list): #this only does one level of nesting
	list_sum = 0
	for i in list:
		list_sum += sum(i)
	return list_sum

def nested_sum(t):
	total = 0
	for i in t:
		if type(i) is int:
			total += i
		else:
			total += nested_sum(i)
	return total


t = [[1,[2,3]],[4,5,6],[7,8,9,10]]
print nested_sum(t)