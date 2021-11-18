import numpy as np

def add_intercept(x):
	new_col = [1 for i in range(len(x))]
	return np.insert(x, 0, new_col, axis=1)

"""Computes the vector of prediction y_hat from two non-empty numpy.array.
Args:
x: has to be an numpy.array, a vector of shape m * 1.
theta: has to be an numpy.array, a vector of shape 2 * 1.
Returns:
y_hat as a numpy.array, a vector of shape m * 1.
None if x or theta are empty numpy.array.
None if x or theta shapes are not appropriate.
None if x or theta is not of the expected type.
Raises:
This function should not raise any Exception.
"""

def predict_(x, theta):
	return np.dot(x, theta)