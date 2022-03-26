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
'''
import random
import torch


model = torch.nn.Sequential(torch.nn.Linear(1,16),
							torch.nn.ReLU(),
							torch.nn.Linear(16,1),
							torch.nn.ReLU())

def agent(state):
	action = model(state)
	return action

def env(action=None):
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
	elif new_state > 8 or new_state < 0: return state, 0, False
	# normal
	else: return new_state, 0, False


# set the global variable state
state = 0

for i in range(10):
	done = False
	eprew = 0
	while not done:
		act = agent(state)
		nst, rew, done = env(act)
		state = nst
		eprew += rew
	print(eprew)