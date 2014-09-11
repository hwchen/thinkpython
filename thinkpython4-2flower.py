#thinkpython chapter 4.12 exercises, exercise 4.2
#Draw flowers

#This program draws a flower with number_petals and petal_width and petal_length
#This requires a function to draw the arc (depends on petal length and width)
#and a function to control the overall shape (depends on # of petals)

import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def arc(t, r, angle):
	""" Draws an arc based on a given radius and angle.
		Don't forget float for the angle!
	"""

	arc_steps_number = 50
	arc_steps_turn = float(angle) / arc_steps_number
	arc_steps_length = r*(math.sin(math.radians(arc_steps_turn)))
	
	for i in range(0,arc_steps_number):
		fd(t,arc_steps_length)
		lt(t, arc_steps_turn)

def petal(t, petal_width, petal_length):
	""" Based on petal_width and petal_length, 
		calculates parameters for the arc that will 
		be drawn and calls arc.
		petal_width is a ratio, from 1-100, with 100 creating 
		a petal whose length is the same as width
		petal_length is in pixels.
		radius r is inversely proportional to petal_width 
		angle is proportional to petal_width
		Draws a petal to the LEFT of starting position and 
		reorients.

		This implementation doesn't seem to give the same petal
		length for differing widths though?

	"""

	r = petal_length / (float(petal_width) / 100) 
	angle = 180 * (float(petal_width) / 100)
	
	arc(t, r, angle)
	lt(t, 180 - angle)
	arc(t, r, angle)
	lt(t, 180-angle)



def flower(t, number_petals, petal_width, petal_length):
	""" Creates flower with number_petals, petal_width, petal_length
		Divides up circle according to number_petals.
		In each direction, draws a petal of petal_width and petal_length
		petal width must be between 1 and 100

	"""
	degrees_btwn_petals = 360/float(number_petals)
	print(degrees_btwn_petals)	

	for i in range(number_petals):
		petal(t, petal_width, petal_length)
		lt(t, degrees_btwn_petals)

flower(bob, 7, 100, 50)
wait_for_user()