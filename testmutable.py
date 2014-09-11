
class foo(object):
	def __init__(self, a=[]):
		a.append(5)
		self.bar= []
		self.bar.extend(a)
		
	


a = foo()
b = foo()
c = foo()

print a.bar,b.bar,c.bar
