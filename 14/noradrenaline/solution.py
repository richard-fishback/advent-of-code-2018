#so, already anticipating that this is not going to be efficient enough for part 2, 
# but let's see where we can get with this.
import re

class elf_situation:
    def __init__(self):
        # this is always the same I guess?
        self.recipes = [3,7]
        self.pos = [0,1]
    def progress(self):
        new_score = self.recipes[self.pos[0]] + self.recipes[self.pos[1]]
        if new_score//10 > 0:
            self.recipes.append(new_score//10)
        self.recipes.append(new_score%10)
        # then advance the elves:
        self.pos[0] = (self.pos[0]+1+self.recipes[self.pos[0]])%len(self.recipes)
        self.pos[1] = (self.pos[1]+1+self.recipes[self.pos[1]])%len(self.recipes)
    def check_for_sequence(self,seq):
        # should probably do something like calling this every 100,000 
        # rather than every time
        # freq will only check us the last that many
        p = re.compile(f"({seq})")
        m = p.search(''.join([str(x) for x in self.recipes]))
        if m:
            # get the oneses right
            return m.span()[0]
        else:
            return 0
            
        

learn_iters = 825401 # my input
elfs = elf_situation()
loop_count = 0
check_this_often = 1000000
answer = 0
while answer == 0:# learn_iters + 10 > len(elfs.recipes):
    elfs.progress()
    loop_count += 1
    if loop_count%check_this_often == 0:
        answer = elfs.check_for_sequence(learn_iters)


print("part 1: " + ''.join([str(x) for x in elfs.recipes[int(learn_iters):int(learn_iters)+10]])) 
print(f"part 2: {answer}")


