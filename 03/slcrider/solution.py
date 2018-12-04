from collections import defaultdict
from itertools import product

def process_claims(claims):
    for claim in claims:
        parts = claim.split()
        yield {
            'claim': parts[0],
            'x': int(parts[2].split(',')[0]),
            'y': int(parts[2].split(',')[1][:-1]),
            'width': int(parts[3].split('x')[0]),
            'height': int(parts[3].split('x')[1])
        }

if __name__ == '__main__':
    fabric = defaultdict(list)
    for claim in process_claims([line for line in open('input.txt').readlines()]):
        for (i, j) in product(range(claim['x'], claim['x'] + claim['width']), range(claim['y'], claim['y'] + claim['height'])):
            fabric[(i,j)].append(claim['claim'])
    print('solution 1:', sum([1 for inch in fabric if len(fabric[inch]) > 1]))
    print('solution 2:', list(set([fabric[inch][0] for inch in fabric if len(fabric[inch]) == 1]) - set([fabric[inch][0] for inch in fabric if len(fabric[inch]) > 1]))[0])
