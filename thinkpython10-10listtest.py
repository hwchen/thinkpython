#thinkpython 10.10 list test

"""	generating lists using .append or list + [x] to
	see which is faster. Use the time module.

"""
import time


def test1():
	t = []

	fin = open('words.txt')
	time.clock()
	for line in fin:
		word = line.strip()
		t.append(word)
	return time.clock()

def test2():
	t = []

	fin = open('words.txt')
	time.clock()
	for line in fin:
		word = line.strip()
		t = t + [word]
	return time.clock()

start_time = time.time()
print test1()
finish_time = time.time()
print ('function 1 took ' + str(finish_time - start_time) + ' seconds')

#print test2()
print 'done'



#maybe  t = t + [x] is slower because you also have to create
#another list for [x]?