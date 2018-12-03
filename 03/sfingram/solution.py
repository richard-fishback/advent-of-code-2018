from collections import defaultdict
from dataclasses import dataclass
@dataclass
class Claim:
    id: int
    left: int
    top: int
    width: int
    height: int

    def rasterize(self):
        for x in range(self.width):
            for y in range(self.height):
                yield (self.left + x, self.top + y)

def read_claim(x):
    fields = x.split(' ')
    coords = fields[2].split(',')
    dims = fields[3].split('x')
    return Claim(int(fields[0].split('#')[-1]),
                 int(coords[0]), int(coords[1][:-1]),
                 int(dims[0]), int(dims[1]))

screen = defaultdict(set)
claims = [read_claim(x) for x in open('input.txt')]
for claim in claims:
    for y in claim.rasterize():
        screen[y].add(claim.id)
overlapping_count = sum(1 for x in screen.values() if len(x) > 1)
nonoverlapping_id = next(iter(set(claim.id for claim in claims) -
                              set(y for x in screen.values()
                                  for y in x if len(x) > 1)))
print(f'Part One: {overlapping_count}')
print(f'''Part Two: {nonoverlapping_id}''')
