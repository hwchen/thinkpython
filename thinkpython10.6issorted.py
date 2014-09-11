#Think Python 10.6
# takes a list, returns True if list is sorted in ascending
#order and False otherwise. <>= assumed to work on list.
#make sure to test edge cases! interaction of range and len

def is_sorted(t):
	for i in range(len(t)-1):
		if t[i] > t[i+1]:
			return False
	return True

t = [1,2,3,4,5,4]
print is_sorted(t)