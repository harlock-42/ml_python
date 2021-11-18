import numpy as np

def predict(x, theta):
	res = np.zeros(x.shape)
	for i, nb in enumerate(x):
		res[i] = theta[0] + theta[1] * nb
	return res

"""Computes a gradient vector from three non-empty numpy.array, without any for-loop.
The three arrays must have compatible shapes.
Args:
x: has to be an numpy.array, a vector of shape m * 1.
y: has to be an numpy.array, a vector of shape m * 1.
theta: has to be an numpy.array, a 2 * 1 vector.
Return:
The gradient as a numpy.array, a vector of shape 2 * 1.
None if x, y, or theta are empty numpy.array.
None if x, y and theta do not have compatible shapes.
None if x, y or theta is not of the expected type.
Raises:
This function should not raise any Exception.
"""

def simple_gradient(x, y, theta):
	if isinstance(x, np.ndarray) == False or isinstance(y, np.ndarray) == False or isinstance(theta, np.ndarray) == False:
		return None
	if x.ndim != 1 or y.ndim != 1 or theta.ndim != 1:
		return None
	if theta.shape[0] != 2:
		return None
	y_hat = predict(x, theta)
	grad = np.zeros(2)
	grad[0] = (1.0 / len(y)) * sum(y_hat - y)
	grad[1] = (1.0 / len(y)) * sum((y_hat - y) * x)
	return grad