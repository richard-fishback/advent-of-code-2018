import numpy as np

a = np.array([[int(x.split(', ')[0]),int(x.split(', ')[1])] for x in open('input.txt')])

def closest(p,centers):
    # take point p, return -1 if point is closest to two centers, 
    # or the index of the nearest point otherwise
    dists = [sum(abs(p-c)) for c in centers]
    min_dist = min(dists)
    if sum([1 for x in dists if x == min_dist]) == 1:
        return np.argmin(dists)
    else:
        return -1
# label space
space = np.array([[closest(np.array([x,y]),a) for y in range(np.amax(a,0)[1])] for x in range(np.amax(a,0)[0])])

# parse space: get the largest that is not adjacent to an edge:
maxsize = 0
maxpoint = -1
for i in range(len(a)):
    if (i not in space[0,:] and i not in space[:,0] and i not in space[-1,:] and i not in space[:,-1]):
        sz = sum(sum(space==i))
        if sz > maxsize:
            maxsize = sz
            maxpoint = i

print("part 1: " + str(maxsize))

# next paint the distances.
def dist_sum(p,centers):
    return sum([sum(abs(p-c)) for c in centers])

# label space
dspace = np.array([[dist_sum(np.array([x,y]),a) for y in range(np.amax(a,0)[1])] for x in range(np.amax(a,0)[0])])

# check that I have allotted enough space
# if any 10000s are along the edges then I need to expand the range:
m = 10000
if (sum(dspace[0,:]<m) or sum(dspace[-1,:]<m) or sum(dspace[:,0]<m) or sum(dspace[:,-1]<m)):
    print("PROBLEM: you didn't allot enough space!")

# assuming that's fine, let's get the size of the region of points who fit the desired sum
print("part 2: " + str(sum(sum(dspace<m))))

