import numpy as np

"""
Description:
Fits the model to the training dataset contained in x and y.
Args:
x: has to be a numpy.array, a vector of shape m * 1: (number of training examples, 1).
y: has to be a numpy.array, a vector of shape m * 1: (number of training examples, 1).
theta: has to be a numpy.array, a vector of shape 2 * 1.
alpha: has to be a float, the learning rate
max_iter: has to be an int, the number of iterations done during the gradient descent
Return:
new_theta: numpy.array, a vector of shape 2 * 1.
None if there is a matching shape problem.
None if x, y, theta, alpha or max_iter is not of the expected type.
Raises:
This function should not raise any Exception.
"""

