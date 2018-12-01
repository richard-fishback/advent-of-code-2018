#!/usr/bin/env python
inputs = []
with open('input') as f:
    for l in f.readlines():
        inputs.append(int(l.strip()))

answer_one = 0
for i in inputs:
    answer_one += i
print(f'answer one: {answer_one}')

v = 0
answer_two = 0
seen = {}
while not answer_two:
    for i in inputs:
        v += i
        if v in seen:
            answer_two = v
            break
        else:
            seen[v] = 1
print(f'answer two: {answer_two}')
