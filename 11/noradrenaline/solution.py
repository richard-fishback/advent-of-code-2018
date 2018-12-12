#import numpy as np
# we could paint space with the relevant values. 
# it's also not a big deal to calculate on the fly, right?
# this is one of those that feels too straightforward, what's the catch.
my_input = 2187

def powerlevel(x,y,serial):
    n = (x+10)**2 * y + (x+10)*serial
    # way 1:
    #d = int(str(n)[-3]) - 5
    # way 2:
    d = n//100 - n//1000*10 - 5
    return d

# so I don't actually need to save coordinates, just calculate the max
coords = [0,0]
max_sum = -46 # can't be lower than this
for x in range(1,299):
    for y in range(1,299):
        s = sum([sum([powerlevel(x+dx,y+dy,my_input) for dx in range(3)]) for dy in range(3)])
        if s > max_sum:
            max_sum = s
            coords = [x,y]

print(f"part 1: {coords[0]},{coords[1]}")

# hm, now for this it does feel like precomputing is the right thing to do
import numpy as np
powergrid = np.array([[powerlevel(x,y,my_input) for y in range(1,301)] for x in range(1,301)])

def find_answer(powergrid):
    coords_plus = [0,0,0]
    max_sum_plus = -5*300*300 # can't be lower than this
    for sz in reversed(range(1,301)):
        # if at any point the maximum sum is greater than the possible max, we can stop:
        if max_sum_plus >= 4*sz*sz:
            return coords_plus
        for x in range(0,301-sz):
            for y in range(0,301-sz):
                s = sum(sum(powergrid[x:x+sz,y:y+sz]))
                if s > max_sum_plus:
                    max_sum_plus = s
                    coords_plus = [x+1,y+1,sz]
    return coords_plus

c = find_answer(powergrid)
print(f"part 2: {c[0]},{c[1]},{c[2]}")

# ugh. This worked, but it's not as fast as I might wish.
# counting down really only saved us a few iterations, we got all the way down to size 4 
# before we stopped.

# I feel like maybe you could make some sort of statistical argument that the data is distributed 
# evenly enough that the probability that you find a max in a square bigger than, say, 30x30 is highly
# unlikely, but I'm not sure exactly how to justify that.

# probably there's an image toolbox that kernel sums faster than this clunky way.

# come to think of it, we didn't really need the -5 part of the calculation.
# not that that was in any way limiting

from scipy import signal

m = -5*300*300
for i in range(1,300):
    print(f"trying {i}")
    mhere = np.amax(signal.convolve2d(powergrid,np.ones([i,i]),mode='valid'))
    if mhere > m:
        m = mhere
        final_i = i

print(f"final_i: {final_i}")
# this was considerably faster than above, although still not like fantastic.
# there'd be another step to actually get the coordinates.
# I am not impressed enough with this speed-up to finish reimplementing the whole thing. It's night time.
