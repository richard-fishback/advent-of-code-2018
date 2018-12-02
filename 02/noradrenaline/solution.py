import numpy as np# solution for part 1
a = [x.strip() for x in open('input.txt')]
def hasn (str):
    m = {}
    for x in str:
        if x in m:
            m[x] = m[x]+1
        else:
            m[x] = 1
    r = np.array([0,0])
    if 2 in m.values():
        r[0] = 1
    if 3 in m.values():
        r[1] = 1
    return r

def match(str1,str2):
    # in matlab I would have used so much logical indexing
    # I'm sure numpy has this
    x = np.array([c for c in str1])
    y = np.array([c for c in str2])
    if sum(x != y) == 1:
        return ''.join(x[x==y])
    else:
        return 0

def compare(a):
    for idx,str1 in enumerate(a,1):
        for str2 in a[idx:]:
            u = match(str1,str2)
            if u != 0:
                return u

counts = np.array([0,0])
for str in a:
    counts = counts + hasn(str)
print("part 1 solution: ", counts[0]*counts[1])
print("part 2 solution: ", compare(a))

