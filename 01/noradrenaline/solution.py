with open('input.txt') as inp:
    print(sum([int(x) for x in inp.readlines()]))

with open('input.txt') as inp:
     b = [int(x) for x in inp.readlines()]

# this feels inelegant
s = 0
i = 0
m = {}

while 1:
    if s in m:
        print(s)
        break
    else:
        m[s] = 1
        s = s + b[i]
        i = (i+1)%len(b)

