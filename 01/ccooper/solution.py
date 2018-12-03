#!/usr/bin/env python

frequency = 0

input = open('input.txt')
for line in input.readlines():
    if line[0] == '-':
        line = line[1:]
        val = int(line)
        frequency -= val
    elif line[0] == '+':
        line = line[1:]
        val = int(line)
        frequency += val
freq = str(frequency)
print('Frequency: ' + freq)
