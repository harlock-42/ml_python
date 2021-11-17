import numpy as np

def add_intercept(x):
	new_col = [1 for i in range(len(x))]
	print(x)
	return np.insert(x, 0, new_col, axis=1)

def predict_(y, theta):
	y = add_intercept(y)
	print(y)
	Mat = y * theta
	y_hat = np.zeros(y.shape)
	for i, elem in enumerate(y_hat):
		y_hat[i] = sum(elem)
	return y_hat

def predict(x, theta):
	res = np.zeros(x.shape)
	for i, nb in enumerate(x):
		res[i] = theta[0] + theta[1] * nb
	return res

def loss_elem_(y, y_hat):
	return (y_hat - y) ** 2

def loss_(y, y_hat):
	return (1.0 / (len(y_hat) * 2.0)) * sum(loss_elem_(y, y_hat))