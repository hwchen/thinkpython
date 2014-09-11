#thinkpython chapter 4.12 exercises, exercise 4.4
#Draw Alphabet

#This program draws each letter of the alphabet using arcs and straight lines

"""
Stopping after 2 letters. Things I'd like to add: separate function
for calculating the width and radius so I don't have to do it for 
each letter. If there was a typewriter function, it could be in there.

"""

import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

#components of each letter, abstracted so the can easily be scaled.

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



#Start with drawing the letters
#parameter size is how many pixels high the whole letter is.
#all letters drawn agains left side of letter box, and returned
#to bottom right corner of box. All boxes are half as wide as they
#are tall (this is monospace)

def draw_a(t, size):
	""" 

	"""
	width = .25 * float(size)
	radius = .5 * float(width)

	pu(t)
	fd(t, width)
	lt(t, 90)
	fd(t, radius)
	pd(t)
	arc(t, radius, 360)
	pu(t)
	fd(t, radius)
	lt(t, 180)
	pd(t)
	fd(t, width)
	lt(t, 90)


#draw_a(bob, 500)



def draw_b(t, size):
	""" Draw b
	"""
	
	width = .25 * float(size)
	radius = .5 * float(width)
	
	lt(t)
	pd(t)
	fd(t, size)
	lt(t, 180)
	fd(t, 3 * width)
	fd(t, radius)
	arc(t, radius, 360)
	fd(t, radius)
	lt(t, 90)
	pu(t)
	fd(t, width)
	pd(t)


def draw_space(t, size):
	pu(t)
	fd(t, .1 * size)
	pd(t)

#draw_b(bob, 500)

"""
def draw_c(t, size):
def draw_d(t, size):
def draw_e(t, size):
def draw_f(t, size):
def draw_g(t, size):
def draw_h(t, size):
def draw_i(t, size):
def draw_j(t, size):
def draw_k(t, size):
def draw_l(t, size):
def draw_m(t, size):
def draw_n(t, size):
def draw_o(t, size):
def draw_p(t, size):
def draw_q(t, size):
def draw_r(t, size):
def draw_s(t, size):
def draw_t(t, size):
def draw_u(t, size):
def draw_v(t, size):
def draw_w(t, size):
def draw_x(t, size):
def draw_y(t, size):
def draw_z(t, size):
"""

draw_a(bob, 100)
draw_space(bob, 100)
draw_b(bob, 100)


wait_for_user()