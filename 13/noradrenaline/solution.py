
import numpy as np

turn_rules = {
        '|': {'^':'^','v':'v'},
        '-': {'>':'>','<':'<'},
        '/': {'^':'>','<':'v','v':'<','>':'^'},
        '\\': {'v':'>','<':'^','^':'<','>':'v'},
        '+': {
                0: {'^':'<','<':'v','v':'>','>':'^'},
                1: {'^':'^','<':'<','v':'v','>':'>'},
                2: {'^':'>','>':'v','v':'<','<':'^'}
             }
}


# Let's agree that our axes are as the were in an earlier problem,
#  x -->
# y
# |
# v

direction_map = {
        '^': np.array([0,-1]),
        'v': np.array([0,1]),
        '>': np.array([1,0]),
        '<': np.array([-1,0]),
}

class cart:
    def __init__(self,x,y,carat):
        #self.x = x
        #self.y = y
        self.removed = 0
        self.position = np.array([x,y])
        self.bearing = carat
        self.turn_rule_state = 0 # this is where we keep track of turn rules
    def turn(self,seg):
        # turn based on your current direction (whence you entered seg from) and seg
        if seg == '+':
            self.bearing = turn_rules[seg][self.turn_rule_state%3][self.bearing]
            self.turn_rule_state += 1
        else:
            self.bearing = turn_rules[seg][self.bearing]
    def move(self):
        # then move in the direction you're facing
        self.position += direction_map[self.bearing]

# get the track map:
track = [[c for c in r.rstrip()] for r in open('input.txt').readlines() if len(r) > 1]
# note that this prints right, but you harvest the track element by calling track[y][x] which is whatever.

# get the carts off the track (replace them with - or |)
carats =  {'^':'|','v':'|','>':'-','<':'-'}
carts = []
[[carts.append(cart(x,y,char)) for x,char in enumerate(row) if char in carats] for y,row in enumerate(track)]
track = [[carats[c] if c in carats else c for c in row] for row in track]

def print_track(track):
    [print(''.join(r)) for r in track]
def print_track_with_carts(track,carts):
    # this puts the dang carts back in the track, so do not use in actual operation
    for car in carts:
        track[car.position[1]][car.position[0]] = car.bearing
        print_track(track)

# okay, can we iterate now?
# this has gotten annoyingly complicated, as I knew it would
# I don't even have a working prototype and I want to redesign.
#def go_until_crash(track, carts):
iter_count = 0
collision = 0
removed_carts = 0
while len(carts) - removed_carts > 1:
    iter_count += 1
    carts = sorted(carts, key = lambda x: x.position[1]*1000+x.position[0])
    positions = [c.position for c in carts]
    for i,c in enumerate(carts):
        if c.removed == 1:
            continue
        c.turn(track[c.position[1]][c.position[0]])
        c.move()
        #carts[i] = c # not sure if this is necessary but can't hurt?
        # check for collision:
        if sum([1 for pos in positions if np.all(pos == c.position)]) > 1:
            if collision == 0:
                print(f"part 1: {c.position[0]},{c.position[1]}")
                collision = 1 #erhm...
            # remove the problem carts
            # this is getting dumber by the second
            for i in [i for i,dumb in enumerate(carts) if np.all(dumb.position == c.position)]:
                # I'm hoping this does what I want
                carts[i].removed = 1
                carts[i].position = np.array([-1,-1])
                removed_carts += 1
        else:
            positions[i] = c.position
            
last_cart = sorted(carts, key = lambda x: x.position[1]*1000+x.position[0])[-1]
print(f"part 2: {last_cart.position[0]},{last_cart.position[1]}")
