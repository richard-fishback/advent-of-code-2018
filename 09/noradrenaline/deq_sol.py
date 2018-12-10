from collections import deque

last_marb = 7105800
num_players = 411

scores = [0 for x in range(num_players)]
marble_array = deque([0])
current_pos = 0
divisor = 23
current_player = 0

for i in range(1,last_marb+1):
	current_player = (current_player+1)%num_players
	if i%divisor == 0:
		marble_array.rotate(7)
		scores[current_player] += i + marble_array.popleft()
	else:
		marble_array.rotate(-2)
		marble_array.appendleft(i)

print(max(scores))



