#thinkpython 14.6, zipcode using urllib

import urllib
import string

#conn = urllib.urlopen('http://thinkpython.com/secret.html')
#for line in conn:
#	print line.strip()

def zipinfo(zipcode):
	"""zipcode(str) is arg, outputs tuple of city name 
	and population, str and int respectively"""
	
	url = 'http://www.uszip.com/zip/' + zipcode
	conn = urllib.urlopen(url)
	#readlines or iterating goes to the end of the file. Need to reinit
	#if i want to read the file again. Probably	
	#Also, searching for 'population' doesn't work...
	#for line in conn.fp:
	#	if 'population' in line:
	#		print line

	html = conn.read()

	#title holds city name + ' zip code'
	
	citystart = html.find('<title>') + 7
	cityend = html.find(' zip code')
	cityname = html[citystart:cityend]	

	#popultion is in a tag after 'Total Population

	popstart = html.find('Total population') + 25
	popend = html.find('Total population') + 35
	population = html[popstart:popend]
	population = population.strip()
	population = population.translate(None,'<>/')
	population = population.translate(None,string.ascii_letters)

	conn.close()
	return (cityname, population)

if __name__ == '__main__':
	userinput = raw_input('enter zipcode: ')
	print(zipinfo(userinput))
