#thinkpython chapter 15, rectangles and OO

import math
from swampy.World import World

#15.1, points

class Point(object):
	"""represents a point in 2-d space"""

def distance_between_points(pt1, pt2):
	"""Takes two Point instances with attributes x and y, finds the distance
	btwn the points"""
	
	diffx = abs(pt1.x - pt2.x)
	diffy = abs(pt1.y - pt2.y)
	
	return math.sqrt(math.pow(diffx, 2) + math.pow(diffy,  2))

#15.2 rectangle

class Rectangle(object):
	"""represents a rectangle with width, height, and coordinates of lower left."""

def move_rectangle(rect, dx, dy):
	"""Takes instance of Rectangle rect, and ints dx and dy. Moves the coordinate"""

	rect.corner.x = rect.corner.x + dx
	rect.corner.y = rect.corner.y + dy

	#It's an alias, so don't have to return anything

def move_rectangle_copy(rect, dx,dy):
	"""creates a copy of rect(instance of Rectangle), moves it by dx and dy, 
	and returns the copy"""

	box = copy.copy(rect)
	box.corner.x = box.corner.x + dx
	box.corner.y = box.corner.y + dy
	
	return box 	

def draw_rectangle(canv, rect, color='green4'):
	"""canv is Canvas object, rect is Rectangle object. draw rectangle on
	the canvas"""
	pt1 = []
	pt2 = []
	bbox = []
	
	pt1.append(rect.corner.x)
	pt1.append(rect.corner.y)
	pt2.append(rect.corner.x + rect.width)
	pt2.append(rect.corner.y + rect.height)

	bbox.append(pt1)
	bbox.append(pt2)
	
	canv.rectangle(bbox, outline='black', width=2, fill=color)
	
def draw_point(canv,pt):
	"""Takes a canvas, draw a circle on the point"""
	center = []
	center.append(pt.x)
	center.append(pt.y)

	canv.circle(center, 2, outline = 'black', fill = 'black')

class Circle(object):
	"""Class circle has attributes center, radius. Center is object Point"""

def draw_circle(canv,circ):
	"""on object canvas (canv), draw object circle (circ)"""
	
	center = []
	center.append(circ.center.x)
	center.append(circ.center.y)
	radius = circ.radius
	canv.circle(center, radius, outline = 'black')



if __name__ == '__main__':
	
	rect = Rectangle()
	rect.width = 100
	rect.height= 100
	rect.corner = Point()
	rect.corner.x = 0
	rect.corner.y = 0	
	
	pt1 = Point()
	pt1.x = 0
	pt1.y = 0	

	circ = Circle()
	circ.center = Point()
	circ.center.x = 0
	circ.center.y = 0
	circ.radius = 20



	# for czeh flag
	
	world = World()
	canvas = world.ca(width=500, height=500, background='white')
	#bbox = [[-150,-100], [150,100]]
	#canvas.rectangle(bbox, outline='black', width=2, fill='green4')
	#canvas.circle([-25,0], 70, outline=None, fill='red')
	#draw_rectangle(canvas, rect, 'green1')
	#draw_point(canvas, pt1)
	#draw_circle(canvas, circ)	
	

	#Czech flag (can refactor into its own function)
	box1 = [[0,0],[200,150]]
	box2 = [[0,0],[200, 75]]
	triangle = [[0,0],[100,75],[0,150]]

	canvas.rectangle(box1, outline='black', width=2)
	canvas.rectangle(box2, outline='black', width=2, fill = 'blue')
	canvas.polygon(triangle, outline='black', width=2, fill='red')
	
	world.mainloop()
