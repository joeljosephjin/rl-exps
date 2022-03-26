import torch
from copy import deepcopy


# taskset
x = torch.tensor([[-15.0], [0.0], [15.0], [7.0]])
taskset = []
# for a,b in [(-7.0, 2.0),(-2.0, 7.0),(7.0, 2.0),(2.0, 7.0),(15.0, 7.0),(7.0, 15.0)]: # 6
for a,b in [(-7.0, 2.0),(-7.0, 7.0), (-7.0, -6.0)]:
	y = a*x + b
	taskset.append([x,y])
# taskset


# define the NN
w_init = torch.tensor(9.0, requires_grad=True)
b_init = torch.tensor(8.0, requires_grad=True)
lossfn = torch.nn.MSELoss()
# define the NN


# training loop
for _ in range(200):
	meta_loss = 0

	# for each task
	for X,Y in taskset:

		# w <-clone- w_init
		w = w_init*1.0; b = b_init*1.0
		w.retain_grad(); b.retain_grad()

		# adaptation update
		Y_pred = w*X[:-1] + b; loss = lossfn(Y[:-1], Y_pred)
		w.grad, b.grad = None, None; loss.backward(retain_graph=True)
		w.data -= w.grad*0.001; b.data -= b.grad*0.001

		# prepare meta-loss
		Y_pred = w*X[-1] + b; loss = lossfn(Y[-1], Y_pred)
		meta_loss += loss

	# meta-update
	w_init.grad = None; b_init.grad = None
	meta_loss.backward()
	print('w_init, b_init w_init.grad:', w_init, b_init, w_init.grad)
	w_init.data -= w_init.grad*0.001; b_init.data -= b_init.grad*0.001
	print(meta_loss.item())

