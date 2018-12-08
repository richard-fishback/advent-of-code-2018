from itertools import chain
import numpy as np
from sklearn.neighbors import NearestNeighbors

points = [list(int(coord) for coord in point.strip().split(', ')) for point in open('input.txt')]

lower_left = [min(point[0] for point in points), min(point[1] for point in points)]
upper_right = [max(point[0] for point in points), max(point[1] for point in points)]
width = upper_right[0] - lower_left[0] + 1
height = upper_right[1] - lower_left[1] + 1
samples = [(x, y) for y in range(lower_left[1], upper_right[1] + 1)
           for x in range(lower_left[0], upper_right[0] + 1)]

nn = NearestNeighbors(1, metric='manhattan')
nn.fit(points)
lookups = nn.kneighbors(samples, return_distance=False)

border = set(chain(lookups[:width, 0],
                   lookups[width * (height - 1):width * height, 0],
                   lookups[:width * height:width, 0],
                   lookups[width - 1:width * height:width, 0]))
max_non_border_area = sorted({i[0]: len(lookups[lookups == i[0]])
                              for i in enumerate(points)
                              if i[0] not in border}.items(),
                             key=lambda x: x[-1])[-1][-1]

print(f'Part One: {max_non_border_area}')

nn = NearestNeighbors(len(points), metric='manhattan')
nn.fit(points)
regions_lt_10k = sum(np.sum(nn.kneighbors(samples, return_distance=True)[0], 1) < 10000)

print(f'Part Two: {regions_lt_10k}')