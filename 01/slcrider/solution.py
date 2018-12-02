def find_first_dup(freqs):
    offsets = {}
    offset = 0
    while True:
        for freq in freqs:
            offset += freq
            if offset in offsets:
                return offset
            offsets[offset] = 1

if __name__ == '__main__':
    freqs = [int(line) for line in open('input.txt')]
    print('first solution:', sum(freqs))
    print('second solution:', find_first_dup(freqs))
