#think python 12.6 a word thats reduced to one letter, and
#each reduction of one letter is also a word
#Why does my solution take 40 minutes while
#his solution takes 1 second?

def open_file(filename = 'words.txt'):
	#returns a list of all words im text file
	
	fin = open(filename)
	t = []
	
	for line in fin:
		word = line.strip()
		t.append(word)
		
	return t

def word_children(word):
	#takes a word type string, gives back a list of all
	#words that can be made by taking away one letter.
	
	t = []
	
	for i in range(len(word)):
		t.append(word[:i] + word[i+1:])
	return t
	
def reducible(word, wordlist, memoize):
	#recursively finds if a word is reducible. memoizes words 
	#that are. returns word
	# bool : string
	#wordlist : list
	#memoize : dict
	# for each word, checks if children are reducible. only choose 
	#real words, otherwise a non-word will return false and stop
	#the whole operation prematurely. with onky real words being tested,
	#false will be thrown if there are no real children, and for real
	#words will go to the base case
	
	
	if word == '':
		return True 
	elif word in memoize:
		return True 
	for i in word_children(word):
		if i in wordlist: #important, otherwise returns false from non-words
			isreducible = reducible(i,wordlist,memoize)
			if isreducible:
				memoize[i]= 0
			return isreducible
	return False #since this is the last thing called it won't 
								#be false unless no true is returned'
								
								
def largest_reducible(wordlist, memoize):
	#creates list of reducible words sorted. returns largest word.
	
	t = []
	
	for word in wordlist:
		if reducible(word, wordlist, memoize):
			t.append((len(word),word))
	
	t.sort(reverse=True )
	
	return t[0][1]
	
if __name__ == '__main__':
	memoize = {}
	wordlist = open_file()
	
	print largest_reducible(wordlist,memoize)
	
	#print reducible('abased', wordlist, memoize)
