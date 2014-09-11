#Thinkpython chapter 14, Files, small problems
import anagram_sets
import os
import shelve
import pprint
#14.1

def walk(dirname):
	"""Prints all the files in subdirectoriese"""
	directory = os.walk(dirname)
	for root, dirs, files in directory:
		 for file in files:
			print os.path.join(root, file)

#14.2
#Should only use one try/except
#Didn't test this one because it's a pain to get the files set up.

def sed(pattern_string, replacement_string, file1, file2):
	"""Read first file and copy to the second file. If pattern string
	appears in the first file, replace it with the second string
	when writing to the second file"""

	try:
		fin = open(file1)
		text = fin.read()
		text = text.replace(pattern_string, replacement_string)
		fin.close()
	except:
		print 'problem with file 1'

	try:
		fout = open(file2, 'w')
		fout.write(text)
		fout.close()	

	except:
		print 'problem with file 2'

#14.3 anagram_db.py
#In his solution he doesn't close the db!
#This one I also didn't check, too lazy to set up
#test, and it's a simple functions

def store_anagrams(d, filename):
	"""Stores anagrams on a shelf
	d: map of anagrams
	filename: str name of shelf"""

	db = shelve.open(filename)
	for word in d:
		db[word] = d[word]
	
	db.close()

def read_anagrams(word, filename):
	"""reads from a shelf stored in file 'filename'
	returns: list of anagrams for word """

	db = shelve.open(filename)
	sig = anagram_sets.signature(word)
	
	try:
		t = db[sig]
		db.close()
		return t
	except:
		db.close()		
		return []


#14.4 Find duplicate files
#could refactor. Later...

def find_suffix(dirname, suffix):
	"""Given str dirname, finds all files in subdirectories that
	have a given suffix."""
	
	t = []
	for root, directory, files in os.walk(dirname):
		for filename in files:
			if suffix in filename:
				t.append(os.path.join(root,filename))
	return t
	
def find_duplicates(dirname):
	"""Given a str dirname, finds all files in that directory and sub
	that are duplicates, printing out the pathname in a list of tuples."""

	d = {} #map of md5sum to filename 
	for root, directory, files in os.walk(dirname):
		for filename in files:
			fullpath = os.path.join(root, filename)
			cmd = 'md5sum ' + fullpath
			fp = os.popen(cmd)
			md5 = fp.read()
			md5 = md5[:32] 
			d.setdefault(md5,[]).append(fullpath) 
	pprint.pprint(d)
	
	t = []
	for i in d:
		if len(d[i]) > 1:
			t.append(d[i])
	return t

	
		
	
if __name__ == '__main__':
	#walk('/home/hwchen/dropbox/')
	#print find_suffix('/home/hwchen/dropbox/projects/thinkpython', 'txt')
	print find_duplicates('/home/hwchen/dropbox/projects/thinkpython')
