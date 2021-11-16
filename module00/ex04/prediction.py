import numpy as np

def add_intercept(x):
	new_col = [1 for i in range(len(x))]
	return np.insert(x, 0, new_col, axis=1)

def predict_(x, theta):
	x = x.reshape((len(x), 1))
	x = add_intercept(x)
	Mat = x * theta
	res = [0.0 for i in range(len(Mat))]
	Res = np.array(res)
	for i, elem in enumerate(Mat):
		Res[i] = sum(elem)
	return Res