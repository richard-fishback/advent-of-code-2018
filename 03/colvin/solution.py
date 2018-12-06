#!/usr/bin/env python

import re


def parse_claim(s):
    r = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    g = r.match(s).groups()
    return {
        'id': int(g[0]),
        'lpos': int(g[1]),
        'tpos': int(g[2]),
        'w': int(g[3]),
        'h': int(g[4])
    }


def print_claim(data, x, y):
    for row in range(y):
        for col in range(x):
            if data[row][col]:
                print(data[row][col], end="")
            else:
                print(".", end="")
        print()


claims = [parse_claim(i.strip()) for i in open('input.txt')]
space = [[0 for x in range(1000)] for y in range(1000)]
overlap = 0

for claim in claims:
    for row in range(claim['tpos'] - 1, claim['tpos'] - 1 + claim['h']):
        for col in range(claim['lpos'] - 1, claim['lpos'] - 1 + claim['w']):
            space[row][col] += 1

#print_claim(space, 270, 1000)

for row in range(1000):
    for col in range(1000):
        if space[row][col] >= 2:
            overlap += 1

print("overlap: {}".format(overlap))

for claim in claims:
    claim_overlap = 0
    for row in range(claim['tpos'] - 1, claim['tpos'] - 1 + claim['h']):
        for col in range(claim['lpos'] - 1, claim['lpos'] - 1 + claim['w']):
            if space[row][col] > 1:
                claim_overlap += 1
    if claim_overlap == 0:
        print("no overlap: id {}".format(claim['id']))
