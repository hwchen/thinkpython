##thinkpython chapter 4.12 exercises, exercise 4.5
#Archimedean spiral

#This program draws an Archimedian spiral
#It ended up being more of a logarightmic spiral. will continue to 
#think about how to make it an Archimedian spiral.

import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def chaos(t, sep_constant, turns):
	""" A ray traced through the spiral intersects at 
		equal distances from each intersection.
		This means that the spiral's arc (radius) increases
		slowly over 360 degrees. I'll do it over 50 steps.
		So, each step I add a constant that is related to the 
		separation distance. Otherwise, should be just like 
		drawing a circle

		Also, the separation distance should be scaled to 
		the size of each step in the approximation

	"""
	#this one has some interesting properties. It's like Chaos and attractors.
	steps = 5000
	
	step_length = 10
	turn_angle = 10  

	for i in range (steps):
		fd(t, step_length)
		lt(t, turn_angle)
		

def spiral(t, sep_constant, turns):
	""" A ray traced through the spiral intersects at 
		equal distances from each intersection.
		This means that the spiral's arc (radius) increases
		slowly over 360 degrees. I'll do it over 50 steps.
		So, each step I add a constant that is related to the 
		separation distance. Otherwise, should be just like 
		drawing a circle

		Also, the separation distance should be scaled to 
		the size of each step in the approximation

		It's a constant moving away from the center. So the change
		in angle between steps should be constant. I just have to find
		the right one, that doesn't fly away too fast.

	"""
	
	steps = 5000
	
	step_length = 10
	turn_angle = 15  

	for i in range (steps):
		fd(t, step_length)
		lt(t, turn_angle)
		turn_angle = float(turn_angle) - .002

spiral(bob, 18000, 100)
wait_for_user()