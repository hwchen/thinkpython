#think python 10.4,5


# 10.4 Takes a list, returns the middle in a new list
# (first and last elements removed)

def middle(t):
	newlist = []
	for i in t:
		newlist.append(i)
	del newlist[0]
	del newlist[len(newlist)-1]
	return newlist

t = [1,'string', 4,5,'tt']
#print middle(t)
#print t

#10.5 Chop takes a list, modifies it by returning first and last
# elements, and returns None

def chop(t):
	del t[0]
	del t[len(t)-1]


a = chop(t)
print t
print a

