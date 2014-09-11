#Thinkpython exercise 8.9

#Debug iterate

def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False

	i = 0
	j = len(word2) - 1 #reltaionship between len and index

	while j>=0: #remember 0 is an index too, so add =
		print  i, j   #print debug here
		if word1[i] != word2[j]:
			return False
		i = i+1
		j = j-1

	return True

is_reverse('pots', 'stop')