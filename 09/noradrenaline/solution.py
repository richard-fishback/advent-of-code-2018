import time
# just type in the input for this one
last_marb = 71058
num_players = 411

scores = [0 for x in range(num_players)]
marble_array = [0]
current_pos = 0
divisor = 23
current_player = 0 # note that player 0 is actually player num_player

for i in range(1,100*last_marb+1):
    current_player = (current_player+1)%num_players
    if i%divisor==0:
        # backtrack and pop
        current_pos = (current_pos-7)%len(marble_array)
        scores[current_player] += i
        scores[current_player] += marble_array.pop(current_pos)
    else: 
        # handle rotation. the actual length of the circle is increased by 1,
        # so if the new position is EQUAL to the length that's okay, but if it's 
        # one greater then the position actually needs to be 0 
        #current_pos = (current_pos+2)%(len(marble_array)+1)
        current_pos += 2
        if current_pos > len(marble_array):
            current_pos -= len(marble_array)
        marble_array.insert(current_pos,i)
    if i == last_marb+1:
        print("part 1: " + str(max(scores)))
    # print(f"{current_player}:\t" + "\t".join([f"({x})" if p == current_pos else str(x) for p,x in enumerate(marble_array)]))
print("part 2: " + str(max(scores)))




