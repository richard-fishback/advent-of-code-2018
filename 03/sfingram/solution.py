from collections import defaultdict
from dataclasses import dataclass
from re import match
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
    return Claim(*(int(y) for y in match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', x).groups()))

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
