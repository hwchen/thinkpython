#Thinkpython Zipf
#first, process the rank order of words in a text. Then graph using 
#matplotlib
import math
import matplotlib.pyplot as plt
import string

def process_file(filename = 'emma.txt', title = 'VOLUME I', footer = 'FINIS'):
	"""Process text into a list"""
	t = []
	
	fin = open(filename)
	s = fin.read()
	header_end = s.rfind(title)
	footer = s.rfind(footer)

	s = s[header_end:footer]
	s = s.replace('-', ' ')
	s = s.translate(None,string.punctuation)
	s = s.lower()
	return s.split()

def word_hist(t):
	"""Takes a list of words, returns a map of words to frequency"""

	d = {}	
	
	for word in t:
		d[word] = d.get(word,0) + 1
	
	return d 

def word_graph(d):
	"""Takes a map of words to frequency, print words in order of 
	rank and graphs the log of frequency versus log of rank""" 
	
	t = []
	
	for x,y in d.items():
		t.append((y,x))
	
	t.sort(reverse = True)
	
	#generate list of log frequency
	logfreq = []
	for i,j in t:
		logfreq.append(math.log(i))

	#generate list of log rank
	logrank = []
	for n in range(1, len(t)+1):
		logrank.append(math.log(n))

	plt.plot(logrank,logfreq)
	plt.xlabel('log rank')
	plt.ylabel('log freq')
	plt.show()

	return t

if __name__ == '__main__':
	text_list = process_file()
	hist = word_hist(text_list)
	word_graph(hist)
	
