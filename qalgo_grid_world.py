'''
-------
| | |R|
-------
| |F| |
-------
|S| | |
-------
678
345
012

garbage: it doesnt work
'''
import random


def agent(state):
	if random.random() > 0.00000001:
		action = random.randint(0,3)
	else:
		action = policy[state]
	return action

def env(action=None):
	if steps == 40: print('forced ending'); return state, 0, True
	# right
	if action == 0: new_state = state + 1
	# up
	elif action == 1: new_state = state + 3
	# left
	elif action == 2: new_state = state - 1
	# down
	elif action == 3: new_state = state - 3
	# goal
	if new_state == 8: return new_state, 10, True
	# danger
	elif new_state == 4: return new_state, -5, False
	# fell outside
	elif new_state > 8 or new_state < 0: return state, -3, False
	# normal
	else: return new_state, -3, False


# set the global variable state
state = 0

qtable = [[0]*4 for _ in range(9)]
count = [[0]*4 for _ in range(9)]

policy = [0]*9

buffer = []

for i in range(300):
	done = False
	eprew = 0
	state = 0
	steps = 0
	while not done:
		steps += 1
		# act = policy[state]
		act = agent(state)
		nst, rew, done = env(act)
		buffer.append([state, act, rew])
		state = nst
		eprew += rew
	print(eprew)

	G=0
	for state, act, rew in buffer[::-1]:
		# print(state, act, rew); import sys; sys.exit()
		G = 0.99*G + rew
		count[state][act] += 1
		qtable[state][act] = ((count[state][act]-1)*qtable[state][act] + G)/count[state][act]
		policy[state] = qtable[state].index(max(qtable[state]))

	print(qtable)
	print(count)
	print(policy)

