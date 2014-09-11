#thinkpython 17.8, 3d graph.

from visual import *
from color_list import read_colors

scene.range = (256,256,256)
scene.center = (128,128,128)


#t = range(0,256,51)
#for x in t:
#    for y in t:
#        for z in t:
#            pos = (x,y,z)
#            color = (1*float(x)/256, 1*float(y)/256, 1*float(z)/256)
#            sphere(pos=pos, radius=10, color=color)
#            print color

colors = read_colors()[0]

print colors
for key, value in colors.items():
    x = int(value[1:3], 16)
    y = int(value[3:5], 16)
    z = int(value[5:], 16)
   
    pos = (x,y,z)
    color = (1*float(x)/256, 1*float(y)/256, 1*float(z)/256)
    sphere(pos=pos, radius=10, color=color)
    print color
