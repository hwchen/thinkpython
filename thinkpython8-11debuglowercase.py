#Think Python exercise 8.11

#Debug following functions which are supposed to find any lowercase
#letters in a string

#This one was really good practice! Good to see where I went wrong.
#I missed the return breaking out of the loops when I first did
#the problems. 3 i was sloppy about having a temp "counting or sum" 
#variable. number 4 was tricky, i understand now.


#This one seems correct. Oops, not correct because loop is broken first time through
# with return statements.
def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True
		else:
			return False


#Since this one puts variable in quotes, it will always return the string 'True'
def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'


#This one seems correct. oops Not correct because will return whether the 
#last value is a lowercase
def any_lowercase3(s):
	for c in s:
		flag = c.islower()
	return flag

#Should return an error, can't have "or" operator in an assignment
#oops, correct. once flag is set to true, the "or" lets it stay
#through the loop. Interesting!

def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

#seems correct. oops, not correct. breaks out of loop early
#if there is any uppercase letter.
def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False
	return True

print any_lowercase5('aa')