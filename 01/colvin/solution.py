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
found = 0
while True:
    if found:
        break
    for i in inputs:
        v += i
        if v in seen:
            answer_two = v
            found = 1
            break
        else:
            seen[v] = 1
print(f'answer two: {answer_two}')
