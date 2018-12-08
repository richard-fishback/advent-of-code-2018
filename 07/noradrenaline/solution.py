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
        return op
    def process(self):
        while len(self.pending) > 0:
            self.iterate()
        return ''.join(self.past)



print("part 1: " + situation('input.txt').process())


# well past the balmer peak here tbh

class situation_with_helpers:
    def __init__(self,filename,num_helps):
        self.past = []
        restr = re.compile("Step (\w+) must be finished before step (\w+) can begin.")
        self.rules = [restr.match(row).groups() for row in open(filename)]
        self.remaining = set([x[0] for x in self.rules]+[x[1] for x in self.rules])
        self.totaltime = 0
        self.helpertime = [0 for i in range(num_helps)]
        self.helperops = [0 for i in range(num_helps)]
        self.timemap = {letter:61+t for t,letter in enumerate(sorted(self.remaining))}
        self.timemap['wait'] = 9999 # ample
        # I did check, we have all 26 letters represented so this lazy way of mapping works.
    def assign(self,helper):
        # worker gets first available operation
        # will need to call this for each 0 in helpertime to make sure everyone picks something up
        blocked_ops = set([x[1] for x in self.rules])
        open_ops = sorted(self.remaining-blocked_ops)
        if len(open_ops)>0:
            op = open_ops[0]
        else:
            op = 'wait'
        self.helperops[helper] = op
        self.helpertime[helper] = self.timemap[op]
        self.remaining -= {op}
    def complete(self,helper):
        # this will check in a completed work
        # will need to call this for each 0 in helpertime I reckon
        op = self.helperops[helper]
        self.past.append(op)
        self.rules = [x for x in self.rules if x[0] != op]
        # when a step completes, re-activate any waiting workers
        # self.helpertime = [0 if self.helperops[i]=='wait' else self.helpertime[i] for i in range(len(self.helpertime))]
    def step(self):
        # move time forward
        # by how much?
        t = min(self.helpertime)
        # could add something in here to allow workers to wait idle
        # will do if it's necessary
        self.helpertime = [x - t for x in self.helpertime]
        self.totaltime += t
    def process(self):
        while len(self.remaining) > 0:
            # assign any available workers
            for i in range(len(self.helpertime)):
                # loop through and assign any available ops
                # extra stuff will go into waiting   
                if self.helpertime[i] == 0 or self.helperops[i]=='wait':
                    self.assign(i)
            # step through time to the next point when something finishes:
            # print(str(self.totaltime)+':\t'+ '\t'.join([op for op in self.helperops]))
            self.step()
            # complete what there is to complete
            for i in range(len(self.helpertime)):
                if self.helpertime[i]==0:
                    self.complete(i)

        return self.totaltime

                    
print("part 2: " + str(situation_with_helpers('input.txt',5).process()))

