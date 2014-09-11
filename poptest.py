def poptest(t):
	
	m=0
	while m < (len(t)-1):
		if t[m] == t[m+1]:
			t.pop(m)
		else:
			m += 1
	return t


t = [1,1,2,3,3,4,5,5,5,5,5,5]

print poptest(t)
