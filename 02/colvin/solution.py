#!/usr/bin/env python

inputs = [l.strip() for l in open('input.txt')]
twofers = 0
threefers = 0
for i in inputs:
    chars = {}
    for c in list(i):
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    have_two = False
    have_three = False
    for c in chars:
        if chars[c] == 2 and not have_two:
            twofers += 1
            have_two = True
        elif chars[c] == 3 and not have_three:
            threefers += 1
            have_three = True
        if have_two and have_three:
            break
print("checksum: {}".format(twofers * threefers))

inputs.sort()
diff_by_one = []
diff_pos = 0
for i in range(0, len(inputs)):
    if i == len(inputs) - 1:
        break
    a = inputs[i]
    b = inputs[i + 1]
    diff = 0
    diffp = 0
    for j in range(0, len(a)):
        if a[j] != b[j]:
            diff += 1
            diffp = j
    if diff == 1:
        diff_by_one = [a, b]
        diff_pos = diffp
print("box ids: {}, {}".format(diff_by_one[0], diff_by_one[1]))
print("common letters: {}".format(diff_by_one[0][0:diff_pos] + diff_by_one[0][diff_pos + 1:]))
