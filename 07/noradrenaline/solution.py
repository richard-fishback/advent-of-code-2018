import re
# challenge to self: not numpy (it's so convenient tho....)

class situation:
    def __init__(self,filename):
        self.past = []
        restr = re.compile("Step (\w+) must be finished before step (\w+) can begin.")
        self.rules = [restr.match(row).groups() for row in open(filename)]
        self.pending = set([x[0] for x in self.rules]+[x[1] for x in self.rules])
    def iterate(self):
        # find unblocked operations, select first alphabetical
        blocked_ops = set([x[1] for x in self.rules])
        op = sorted(self.pending-blocked_ops)[0]
        # add to past, remove from pending, remove the blocks
        self.past.append(op)
        self.pending -= {op}
        self.rules = [x for x in self.rules if x[0] != op]
    def process(self):
        while len(self.pending) > 0:
            self.iterate()
        return ''.join(self.past)

print("part 1: " + situation('input.txt').process())
