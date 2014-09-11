#thinkpython chapter 4.3 exercises
import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()


def square (t, length):
	""" Draws a square of length "length" using 
		turtle "t" 
	"""

	for i in range(4):
		fd(t, length)
		lt(t)


def polygon(t,length,n):
	""" Draws a polygon with n sides and each side length n
		using turtle 't'

	"""

	for i in range(n):
		fd(t, length)
		lt(t, (360/n))

#polygon(bob, 100, 5)

def circle(t, r):
	""" Draws a circle with radius r using turtle t.
		The idea is that 'segment' is the length of the straight line
		that the turtle travels before turning inwards. It's calculated
		by dividing the circle arbitrarily into a segment angle 'x'
		and calculating the length of the segment using trig.

	"""

	x = math.radians(360/100)
	segment = r*(math.tan(x))

	print(segment)
	for i in range(100):
		fd(t, segment)
		lt(t, 360/100)


#circle(bob, 100)

def arc(t,r,x):
	""" A more general version of circle. Prints the same circle 
		as in fn circle, but cuts off after x degrees. steps is
		how 360 is divided up, not how each arc is divided.

	"""
	steps = 100
	arc = r*(math.sin(math.radians(360/steps)))

	print(arc)
	for i in range(steps * x/360 ):
		fd(t, arc)
		lt(t, 360/steps)


arc (bob,50, 180)
wait_for_user()