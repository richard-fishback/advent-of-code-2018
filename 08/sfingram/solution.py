from collections import defaultdict


def get_entries():
    with open('input.txt') as f:
        return [int(x) for x in f.readline().strip().split(' ')]


def read_entry(entries):
    num_children = next(entries)
    num_metadata = next(entries)
    if num_children == 0:
        return sum(next(entries) for i in range(num_metadata))
    children_metadata = sum(read_entry(entries) for i in range(num_children))
    return children_metadata + sum(next(entries) for i in range(num_metadata))


print(f'Part One: {read_entry(iter(get_entries()))}')


def read_entry_ref(entries):
    num_children = next(entries)
    num_metadata = next(entries)
    if num_children == 0:
        return sum(next(entries) for i in range(num_metadata))
    children_metadata = defaultdict(int)
    for i in range(num_children):
        children_metadata[i + 1] = read_entry_ref(entries)
    return sum(children_metadata[next(entries)] for i in range(num_metadata))


print(f'Part Two: {read_entry_ref(iter(get_entries()))}')
