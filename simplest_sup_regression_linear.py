import torch

# dataset
x = torch.tensor([[-15.0], [0.0], [15.0]]) #, [7.0], [-8.0], [200.0], [-200.0]])
a,b = 2,7
y = a*x + b
# dataset

# defining the neural network
w = torch.tensor(5.0, requires_grad=True)
b = torch.tensor(5.0, requires_grad=True)
lossfn = torch.nn.MSELoss()
# opt = torch.optim.SGD([w, b], lr=0.0001)
# defining the neural network


for _ in range(100):
	y_pred = w*x + b
	# print('w, b:', w.item(), b.item(), w.grad, b.grad)
	loss = lossfn(y, y_pred)
	print(loss.item())
	# opt.zero_grad()
	w.grad = None
	b.grad = None
	loss.backward()
	# opt.step()
	w.data -= w.grad*0.001
	b.data -= b.grad*0.001


