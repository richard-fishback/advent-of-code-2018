from collections import defaultdict

def count_chars(datum):
    counter = defaultdict(int)
    for d in datum:
        counter[d] += 1
    return set(counter.values())
def differing_chars(a, b):
    return len(set(enumerate(a)) - set(enumerate(b)))
def same_chars(a, b):
    return ''.join([i[1] for i in sorted(set(enumerate(a)) & set(enumerate(b)))])

data = [i.strip() for i in open('input.txt').readlines()]

char_counts = [count_chars(datum) for datum in data]
two_counts = len([i for i in char_counts if 2 in i])
three_counts = len([i for i in char_counts if 3 in i])

print(f'Part One: {two_counts * three_counts}')
print(f'''Part Two: {next(same_chars(i[1], j[1])
                        for i in enumerate(data)
                        for j in enumerate(data)
                        if i[0] < j[0] and differing_chars(i[1], j[1]) == 1)}''')
