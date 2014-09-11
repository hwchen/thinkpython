"""
This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!

"""

#problem is that pouch contents is initialized for the _class
#and not just per instance. Just change it to initialize the list
#inside instead of passing it. It was just assigning
#to an existing list somehow? weird... Check Goodkangaroo,
#functions are only initialized once. So the list was evaluated
#once, then pointed to again and again. Instead, use None 
#as a default for initializing.

#but wait, then why does my example work? appending the already
#initialized list should still be a bug. Oh, I made a typo that 
#wasn't caught? 

#Ah, I understand. In original implementation, pouch_contents
#was aliased directly to the default contents list. If I initialize
#a separate list inside __init__, then that list doesn't reference
# the default contents. So, in aliased implementation, appending to
#the attribute also appends to the default. but in the second, appending
#to the attribute doesn't append to the default. However, it's still a
#little dangerous. Not as safe as just not having mutable default.
#(it's a little harder to figure out in a class).

class Kangaroo(object):
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=[]):
        """initialize the pouch contents; the default value is
        an empty list"""
        contents.append('5')
        self.pouch_contents = []
	self.pouch_contents.extend(contents) 
   
    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print kanga
print roo
print roo.pouch_contents

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.

