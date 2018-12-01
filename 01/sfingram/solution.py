from itertools import cycle
input_data = [int(i) for i in open("input.txt")]
def find_repeat_freq(vals):
    previous_freqs = {}
    cumulative_sum = 0
    for v in cycle(vals):
        cumulative_sum += v
        try:
            return previous_freqs[cumulative_sum]
        except KeyError:
            previous_freqs[cumulative_sum] = cumulative_sum
print(f'Part One: {sum(input_data)}')
print(f'Part Two: {find_repeat_freq(input_data)}')
