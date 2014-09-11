#Think Python exercise 8.12

#ROT13

#This program will shift a letter forward 13 spaces
#so, mod13 will be necessary.

def rotate_word(word, rotate):
	#initialize
	rotated_word = ''

	#convert to numbers
	for letter in word:
		if (ord(letter) + rotate) > 26:
			rotated_word = rotated_word + chr(ord(letter)-(26-rotate))
		else:
			rotated_word = rotated_word + chr(ord(letter)+rotate) 

	return rotated_word

print rotate_word('xyz', 4)

#compare:

"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print rotate_word('cheer', 7)
    print rotate_word('melon', -10)
    print rotate_word('sleep', 9)