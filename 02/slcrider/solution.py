from collections import Counter

def parse_ids(ids):
    for id in ids:
        yield {
            'two': 1 if 2 in Counter(id).values() else 0,
            'three': 1 if 3 in Counter(id).values() else 0,
            'chars': [char for char in id],
            'word': id
        }

def find_common_id(ids):
    for id in ids:
        for token in parse_ids(ids):
            common_chars = [id[char] for char in range(len(id)) if id[char] == token['chars'][char]]
            if len(common_chars) + 1 == len(id):
                return ''.join(common_chars)

if __name__ == '__main__':
    ids = [line for line in open('input.txt').readlines()]

    two_count = 0
    three_count = 0
    for token in parse_ids(ids):
        two_count += token['two']
        three_count += token['three']
    print('first solution:', two_count * three_count)
    print('second solution:', find_common_id(ids))
