#thinkpython 10.7
# is_anagram. Takes two string, compares them, and determines if 
#they contain the same letters. (one is a combo of the other)

#sort both lists? Or just count?

#hehe, I figure this out as I was falling asleep.


def is_anagram(s1,s2):
	"""s1 and 2 are two strings. to see if they're
		anagrams, first compare the lengths of both,
		then convert to lists. copy one list. (don't need to
		because already copied from the string) compare
		letter in first list to second. destroy any matching
		letter in the second list copy. if second list copy
		= [] at the end of the loop, then return true.

	"""
	t1 = list(s1)
	t2 = list(s2)

	for i in t1:
		if i in t2:
			t2.remove(i)
	if t2 == []:
		return True
	return False

s1 = 'mail'
s2 = 'imala'

print is_anagram(s1,s2)