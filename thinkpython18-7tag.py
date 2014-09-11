#thinkpython 18-7 turtle tag

#create tag game importing wobbler

from Wobbler import *
import math
import random

class Tagger(Wobbler):
	"""Wobblers that play tag"""

	def __init__(self, world, speed=1, clumsiness=60, color='red'):
		Turtle.__init__(self,world)
		self.delay = 0
		self.speed = speed
		self.clumsiness = clumsiness
		self.color = color
		if color == 'orange':
			self.it = True
		else: self.it = False

		self.pu()
		self.rt(randint(0,360))
		self.bk(150)

	def steer_origin(self):
		"""Overrides the steer function in Wobbler.
		This one moves towards the origin.
		atan2 gives the angle between pos x axis and (x,y)
		in radians
		self.heading is in degrees, with east as 0"""
		
		angle_to_east = math.degrees(math.atan2(self.y, self.x))
		angle_to_origin = self.heading + (180-angle_to_east)
		self.rt(angle_to_origin)
		
	def steer(self):
		"""Overrides steer function in Wobbler.
		keeps turtles inside boundary
		and points turtle towards another otherwise."""
		
		if self.it == True:
			for turtle in self.world.animals:
				if self != turtle: #important!
					self.tag_other(turtle)

		if (math.floor(self.x) not in range(-110,110)) or (math.floor(self.y) not in range(-110,110)):
			self.steer_origin()
		elif self.it == True:
			self.steer_towards_closest()
		else:
			self.steer_away_from_it()
			self.wobble()			
			self.wobble()	
			self.wobble()
			self.wobble()

	def steer_towards_closest(self):
		"""Steers towards closest turtle"""
		t = []
		current_location = (self.x, self.y)
		for turtle in self.world.animals:
			turtle_coord = (turtle.x, turtle.y)
			dist_to_turtle = distance(current_location, turtle_coord)
			t.append((dist_to_turtle, turtle_coord))

		t.sort()
		target = t[1][1]

		angle = angle_to_target(current_location, target)
		self.rt(self.heading - angle)

	def steer_away_from_it(self):
		"""Steers away from it turtle if closer than 20"""

		current_location = (self.x, self.y)
		target = ()
		for turtle in self.world.animals:
			if turtle.it == True:
				target = (turtle.x, turtle.y)
		
		angle = angle_to_target(current_location, target)
		
		if distance((self.x, self.y), target) < 50:
			self.rt(self.heading - angle + 180)
		else:
			self.rt(10)	

	def tag_other(self, other):
		"""one turtle(self) tags another"""
		if distance((self.x, self.y),(other.x, other.y)) < 5:
			self.fd(220)
			self.it = False
			other.it = True
			
			
		
def angle_to_target(pt1, pt2):
	"""given two tuples, calculates the angle btwn the two with east as 0"""
	return math.degrees(math.atan2((pt2[1]-pt1[1]),(pt2[0]-pt1[0])))	

	
def distance(pt1,pt2):
	"""given two tuples, calculates the distance"""

	return math.sqrt(math.pow(pt1[0]-pt2[0],2) + math.pow(pt1[1]-pt2[1], 2))


if __name__ == '__main__':
	world = make_world(Tagger)
	world.mainloop()
	
	#pt1 = (1,4)
	#pt2 = (4,8)
	#print angle_to_target(pt1, pt2)
