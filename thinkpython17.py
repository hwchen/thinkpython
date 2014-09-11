#thinkpython chapter 17

#17.1 - 5

class Time(object):
	""" time object, represents time in hh:mm:ss"""
	def print_time(self):
		print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def time_to_int(self):
		return 3600*self.hour + 60*self.minute + self.second


class Point(object):
	"""attributes x and y, represent a coordinate"""
	
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return ('(%d,%d)' % (self.x, self.y))

	def __add__(self, other):
		if isinstance(other, Point):
			return self.add_point(other)
		elif isinstance(other, tuple):
			return self.add_tuple(other)

	def __radd__(self, other):
		return self.__add__(other)

	def add_point(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def add_tuple(self, other):
		return Point(self.x + other[0], self.y + other[1])


if __name__ == '__main__':
