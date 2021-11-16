import numpy as np

def add_intercept(x):
	new_col = [1 for i in range(len(x))]
	return np.insert(x, 0, new_col, axis=1)

def predict_(x, theta):
	theta = theta.reshape((1, 2))
	x = x.reshape((len(x), 1))
	x = add_intercept(x)
	Mat = x * theta
	res = [0.0 for i in range(len(Mat))]
	Res = np.array(res)
	for i, elem in enumerate(Mat):
		Res[i] = sum(elem)
	return Res

def loss_(y, y_hat):
	print(y)
	print(y_hat)

x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
print(y_hat1)