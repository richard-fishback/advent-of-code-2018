# solution for part 1:
import numpy as np

def parse_input_row(row):
    # I could make the input its own class but why.
    # let's just agree that we will parse each row
    # into a list of x1 x2 y1 y2 (and row # for part 2)
    # where these will be the bounds of the range
    # we put into tne numpy array
    # man a nice perl regex wouldn't go amiss here.
    s1 = row.split('@')
    s2 = s1[1].split(':')
    s3 = s2[0].split(',')
    s4 = s2[1].split('x')
    return [int(s3[0]), int(s3[0])+int(s4[0]),int(s3[1]),int(s3[1])+int(s4[1]),s1[0]]

cloth = np.zeros([1000,1000])

rows = [parse_input_row(x) for x in open('input.txt')]

for row in rows:
    cloth[row[0]:row[1],row[2]:row[3]] += 1

print("part 1 answer: ",sum(sum(cloth>1)))

for row in rows:
    if sum(sum(cloth[row[0]:row[1],row[2]:row[3]]>1)) == 0:
        print("part 2 answer: ",row[4])
        break
# (a little sloppy bc I didn't strip off the # but that's whatever.)
