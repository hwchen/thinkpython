#thinkpython chapter 5-14 exercises 5-6 Koch

#Koch curve and snowflake

import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def koch_curve(t, x):
	"""Koch curve with initial start length of x and angle of 60 degrees.
		t is turtle

	"""
	if x < 3:
		fd(t, x)
	else:
		koch_curve(t, float(x)/3)
		lt(t, 60)
		koch_curve(t, float(x)/3)
		rt(t, 120)
		koch_curve(t, float(x)/3)
		lt(t, 60)
		koch_curve(t, float(x)/3)

#koch_curve(bob, 100)
#wait_for_user()




def snowflake (t, x):
	for i in range(3):
		koch_curve(t, x)
		rt(t, 120)

#snowflake(bob, 100)
#wait_for_user()


def square_koch(t, x,):
	


	if x < 4:
		fd(t,x)
	else:
		square_koch(t, float(x)/4)
		lt(t, 90)
		square_koch(t, float(x)/4)
		rt(t, 90)
		square_koch(t, float(x)/4)
		rt(t, 90)
		square_koch(t, float(x)/4)
		lt(t, 90)
		square_koch(t, float(x)/4)

square_koch(bob,500)
wait_for_user()






#exercise 5.2
#Question: why won't it let me call a function that already has an argument?
#ah, it wouldn't make sense, because it's a value, and not a function then.
#But would it? think about this. I think I need to pass the argument separately.

#wait, does this have to do with the print string not being a fruitful function?

def do_n(n, repeat):
	if repeat == 0:
		return n()
	else:
		return do_n(n, repeat-1)

def test(test_string):
	print(test_string)

#do_n(test('hello'), 21)


#exercise 5.5

def draw(t, length, n):
	if n==0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)

	draw(t, length, n-1)
	rt(t, 2*angle)

	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

#draw (bob, 10, 5)
#wait_for_user()