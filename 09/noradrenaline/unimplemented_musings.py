# what would be a smarter way to do this?
# say we use the dumb loop to get up to a vector size of like a million, or so
# then can we do operations in bulk? and does that help us?
# our goal number is 7,105,800. 
# the slow dumb way got me into the 2,000,000 range in less than an hour
# but this thing is going to be slowing down exponentially

# the way where I just operate on a vector of positions would I think be linear but was taking more than
# a second per iteration, which is not viable. Was there something wrong in my process or was it fundamentally slow?

# Is there either like a pattern I can exploit or something like that?

# I should have put some sort of indicator in my thing so I could be sure that it's slowing down too much, 
# like "if i > 2,000,000 and i%100000 print i and the time it took to do the last operation"

# cause, like, I'm living in hope that this will work but it won't, let's be real.

# what sorts of pattern might there be. 
# how about this. when we start from a removal near the beginning of the string,
# can I real quick generate the rest of the string in a single step, up until the last insert before we loop?

# it's a determined repeating pattern so i should, right?
# like, if a is the existing marble array and b is the next n values (find out what n is), then from the first insert 
# post-removal (with a0 the starting location):

# (a0) a1 b0 a2 b1 a3 b2 a4 b3 ... up until you go to put b23, (er, b22 by this count... verify this)
# at which point you will instead remove a determined value: 
# b17 a19 b18 a20 b19 a21 b20 a22 (b21)
#      ^^
# a19 will get removed instead of inserting b22
# this pattern repeats, you insert them alternating except skip a19 and b22

# also need to figure out how to allocate points to a given elf

# but generally, what if we do that: we zip together the vector a (an existing game state which we got however, 
# but is pretty long) with b (the equivalent length of next vectors), following that insert pattern - alternating, 
# but skipping the 19th a and 23rd b (have to be careful with how I count, I think at least one of those is off by 1),
# into a preallocated big array.

# this would let me double the size in a single (albeit somewhat costly) operation; I'd have to loop through the thing
# once rather than each time we add a value

# I would still have to handle the following things:
# how to "turn the corner" (easiest answer might be to just move the end of the vector to the beginning?)
# how to know when to stop
# how to attribute a given score event to the right elf

# so here's the pseudocode
# a is a vector of length >> 23 that I got through the old method
# v = zeros([1,len(a)*2) < what exact size though? but I think preallocating is a good idea
# b = starting value (b just counts up)
# b_incr = 0
# i = 0 < the position in the output vector
# v[:i] = a[:i] < the first bit of a doesn't change
# while a_pos < len(a)-23 <-- or something, we'll stop before we need to turn the corner
#   # exit condition should probably be something more like "we hit a b23 and there's not 19 more a's"
#   v[i] = a[a_pos]
#   a_pos++
#   i++ unless (a_pos-starting_a_pos)%23==19 <-- or whatever, figure out exactly what
#   store the removal value for when the elf gets it
#   v[i] = b+b_incr
#   b_incr++
#   i++ unless (b+b_incr)%23==0 <-- or whatever
#   current_elf++ (mod num-elves) (figure out how this interacts with removal)
#   add to current elf's score if it was a removal 
#   

# then, when you finish this cycle,
# make a new v (permute so that the current position is at the beginning) and continue

# if I'm not mistaken, making only a single pass through an existing (albeit big) vector
# shouldn't be tooooooooooooooooooo terrible

# and we can quickly get up to a big size.
# we'll need to print the max score and exit if we get to the target b+b_incr

# I think this should be faster, but it'll be a lot of work to put together and troubleshoot 
# (lots of off-by-one nitpickery possible)
# so I want to think about whether this will likely be much faster 
# (could do a timing experiment if my box wasn't currently tied up trying to run it the slow way)
# and if there is an even better way to do it (like, probably? but if it's too fancy I can't know it)

# lol while I was waiting around for the initiative to actually implement this,
# the slow-as-butt old solution finished.
