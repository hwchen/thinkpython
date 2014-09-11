#Think Python exercise 9.8

#Cartalk mileage puzzle
"""
	The parameters:
	1) 6 digit number
	2)x, last 4 palindrome
	3) x +1, last 5 palindrome
	4)x+2, middle 4 are palindrome
	5)x+3, all 6 palindrome.

"""

def is_palindrome(string):
	""" Takes a number and checks to see if it's a 
		palindrome. 
		then returns true or false.

	"""
	
	if string == string[::-1]:
		return True
	return False

def cartalk():
	""" iterates through 6 figure numbers
		and checks for above parameters

	"""
	for i in range(100000, 1000000-3):
		number = str(i) #convert string
		if is_palindrome(number[2:]):
			number_addone = str(i+1)
			if is_palindrome(number_addone[1:]):
				number_addtwo = str(i+2)
				if is_palindrome(number_addtwo[1:5]):
					number_addthree = str(i+3)
					if is_palindrome(number_addthree):
						print number, number_addone, number_addtwo, number_addthree

cartalk()



#I like his solution because it doesn't have nested if statements
# I see that the way to avoid it is nice looking AND boolean
# and using descriptive function names as much as possible
# descriptive function names increase readability a lot!
# then, it's less about where the conversion is done.
# it's where it's most legible, which is in the deepest
# function, so you don't have to see it when reading
# at the top level.

"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    http://www.cartalk.com/content/palindromic-odometer
"""

def has_palindrome(i, start, len):
    """Returns True if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start).
    """
    s = str(i)[start:start+len]
    return s[::-1] == s
    

def check(i):
    """Checks whether the integer (i) has the properties described
    in the puzzler.
    """
    return (has_palindrome(i, 2, 4)   and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerates the six-digit numbers and prints any that satisfy the
    requirements of the puzzler"""

    i = 100000
    while i <= 999996:
        if check(i):
            print i
        i = i + 1


#print 'The following are the possible odometer readings:'
#check_all()
#print

