fullinput = open('input.txt').readlines()

# better to keep initial state as string, or make a list of ints?
# let's see what happens with the string thing.
initial = fullinput[0].split(' ')[2].strip()

rules = {}

for x in fullinput[2:]:
    s = x.split(' => ')
    rules[s[0]] = s[1].strip()

# extend initial
# growth cannot exceed 40 in either direction, but we may need a little more
status = '.'*42 + initial + '.'*42

def timestep(status, rules):
    return '..' + ''.join([rules[status[x-2:x+3]] for x in range(2,len(status) - 2)]) + '..'

for i in range(20):
    status = timestep(status,rules)

totalplants = sum([i for i, x in enumerate(status,-42) if x == '#'])
print(f"part 1: {totalplants}")


# annnnd... there's no way this dumb strategy is going to work for 50000000000 generations.
# so just visualizing it out, it does look like it eventually forms some patterns that just travel
# so we need to figure out what the pattern is (some variation of #.# separated by at least 3 dots)
# and how far along it will be located (the pattern moves right one unit per time step once it's fully established)

# establish the pattern:
status = '.'*42+initial+'.'*420
establishing_steps = 1;
next_status = timestep(status,rules)
while next_status[1:] != status[:-1]:
    status = next_status
    next_status = timestep(status,rules)
    establishing_steps += 1

# okay. Now where at step # establishing_steps, the status is next_status.
# this involves a sequence of #s which will proceed to move to the right for the
# remaining 5000000000 - estep steps. So the total "score" will just be 
# the score at point estep plus (5000000000-estep)*(number of points) because
# you are just adding that number to each point's contribution to the score.
score_once_established = sum([i for i, x in enumerate(next_status,-42) if x == '#'])
num_pots = sum([1 for x in next_status if x == '#'])
remaining_steps = 50000000000-establishing_steps

final_ans = score_once_established + num_pots*remaining_steps
print(f"part 2: {final_ans}")
