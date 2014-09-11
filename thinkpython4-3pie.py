#thinkpython chapter 4.12 exercises, exercise 4.3
#Draw Pies

#This program draws a pie composed of triangles. So, it's
#a regular polygon with all vertices connected to a center
#point. Should draw like a flower: one slice, then move over
#and draw the next slice. It will have to retrace each spoke
#once.


import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def draw_slice(t, spoke_length, angle):
	""" Draws a triangle slice of a regular polygon.
		From the center, the sides of the triangle are 
		of spoke_length and the edge of the polygon is side_length

	"""

	base_turn_angle = 180 - (float(180-angle)/2) #calculated as the base angles of an isoceles
	tip_turn_angle = 180 - float(angle)
	side_length = math.sin(math.radians(.5*angle)) * spoke_length * 2

	fd(t, spoke_length)
	lt(t, base_turn_angle)
	fd(t, side_length)
	lt(t, base_turn_angle)
	fd(t, spoke_length)
	lt(t, tip_turn_angle)	#back to initial position

def draw_pie(t, number_slices, spoke_length):
	""" Draws a polygon with lines from all vertices to a center point
		number_slices is equal to number of edges
		spoke_length is from center to vertices
		Function will calculate angle and call draw_slice to draw each
		slice

	"""
	angle = float(360)/number_slices

	for i in range(number_slices):
		draw_slice(t, spoke_length, angle)
		lt(t, angle)



draw_pie(bob, 10, 100)
wait_for_user()