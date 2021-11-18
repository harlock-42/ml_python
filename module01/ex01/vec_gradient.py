import numpy as np

def add_intercept(x):
	new_col = [1 for i in range(len(x))]
	New_col = np.array(new_col)
	return np.c_[New_col, x]

def predict_(x, theta):
	return np.dot(x, theta)

"""Computes a gradient vector from three non-empty numpy.array, without any for loop.
The three arrays must have compatible shapes.
Args:
x: has to be a numpy.array, a matrix of shape m * 1.
y: has to be a numpy.array, a vector of shape m * 1.
theta: has to be a numpy.array, a 2 * 1 vector.
Return:
The gradient as a numpy.array, a vector of shape 2 * 1.
None if x, y, or theta is an empty numpy.array.
None if x, y and theta do not have compatible shapes.
None if x, y or theta is not of the expected type.
Raises:
This function should not raise any Exception.
"""

def gradient(x, y, theta):
	if isinstance(x, np.ndarray) == False or isinstance(y, np.ndarray) == False or isinstance(theta, np.ndarray) == False:
		return None
	if x.ndim != 1 or y.ndim != 1 or theta.ndim != 1:
		return None
	if theta.shape[0] != 2:
		return None
	grad = np.zeros(2)
	X = add_intercept(x)
	y_hat = predict_(X, theta)
	res = np.matmul(X, theta) - y
	grad = (np.matmul(np.transpose(X) , res)) * (1.0 / len(y))
	return grad