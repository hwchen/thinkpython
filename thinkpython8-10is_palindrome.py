#Think python exercise 8.10

# one-line is_palindrome

def is_palindrome(word):
	if word == word[::-1]:
		return True
	return False

print is_palindrome("lool")