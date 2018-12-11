

# oh boy. This is a fun one and I have been meaning to figure out how to get matplotlib
# to actually show me a fcking figure, but it may mean I have to abandon the command line.

# first, can I get a sense of what I'm looking at by iterating and finding the smallest space
# that the points ever occupy? 
# this is not guaranteed to be the right point, but it's likely

import re
import numpy as np
inputs = [re.match('position=<(.+)> velocity=<(.+)>.*',i).groups() for i in open('input.txt').readlines()]

positions = np.array([[int(x) for x in p[0].split(',')] for p in inputs])
velocities = np.array([[int(x) for x in p[1].split(',')] for p in inputs])

# we will want to iterate until pts_area reaches a minimum
def pts_area(positions):
    difs = np.amax(positions,axis=0)-np.amin(positions,axis=0)
    return difs[0]*difs[1]

def print_upper_corner(positions, x, y):
    # get the smallest x and y
    edges = np.amin(positions,axis=0)
    img = np.zeros([x,y])
    for p in positions:
        # figured out by trial and error that I had x and y backward
        if p[1] < edges[1]+x and p[0]< edges[0]+y:
            img[p[1]-edges[1],p[0]-edges[0]] = 1
    [print(''.join([' 'if elem == 0 else 'X' for elem in row])) for row in img]

# so just iterate until the area increases instead of decreases (???)
# then backtrack one and print the upper corner

prev_area = pts_area(positions)
positions = positions + velocities
this_area = pts_area(positions)
loop_counter = 0 # we are already one step in, but we will backtrack
while this_area < prev_area:
    positions += velocities
    prev_area = this_area
    this_area = pts_area(positions)
    loop_counter += 1
# backtrack one
positions -= velocities

print("part 1: ")
print_upper_corner(positions,10,70)
print(f"part 2: {loop_counter}")

