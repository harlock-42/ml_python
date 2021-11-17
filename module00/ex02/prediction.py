import numpy as np

"""Computes the vector of prediction y_hat from two non-empty numpy.array. Args:
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

def simple_predict(x, theta):
	res = np.zeros(x.shape)
	for i, nb in enumerate(x):
		res[i] = theta[0] + theta[1] * nb
	return res