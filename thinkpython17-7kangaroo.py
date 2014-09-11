#thinkpython 17-7 kangaroo

#DOn't forget to look again at testmutable.py and BadKangaroo.py

class Kangaroo(object):
	"""attribute pouch_contents"""

	def __init__(self):
		"""initializes attribute pouch_contents to empty list"""
		self.pouch_contents = []

	def put_in_pouch(self, item):
		""" appends item to attribute pouch_contents list"""
		self.pouch_contents.append(item)

	def __str__(self):
		"""string representation of Kangaroo and pouch_contents"""
		s = 'Kangaroo with pouch containing: '
		if len(self.pouch_contents) == 0:
			s += 'nothing'
		else:
			s += '('
			for i in self.pouch_contents:
				s += str(i) + ', '
				s = s[:len(s)-2] + ')'
		return s
def main():
	kanga = Kangaroo()
	roo = Kangaroo()
	kanga.put_in_pouch(roo)
	print kanga	


if __name__ == '__main__':
	main()
