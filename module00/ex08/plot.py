import matplotlib.pyplot as plt
import numpy as np

def predict(x, theta):
	res = np.zeros(x.shape)
	for i, nb in enumerate(x):
		res[i] = theta[0] + theta[1] * nb
	return res
"""Plot the data and prediction line from three non-empty numpy.array. Args:
      x: has to be an numpy.array, a vector of shape m * 1.
      y: has to be an numpy.array, a vector of shape m * 1.
      theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
        Nothing.
    Raises:
      This function should not raise any Exception.
"""

def plot_with_loss(x, y, theta):
	fig = plt.figure()
	ax = plt.axes()
	x_min = x[0]
	x_max = x[len(x) - 1]
	y_min = x[0] * theta[1] + theta[0]
	y_max = x[len(x) -1] * theta[1] + theta[0]
	plt.plot([x_min, x_max], [y_min, y_max])
	y_hat = predict(x, theta)
	for i, val in enumerate(x):
		plt.plot([val, val], [y[i], y_hat[i]], "r--",)
	plt.scatter(x, y)
	coef = 1.0 / len(x)
	dot_prod = np.dot((y_hat - y), (y_hat - y))
	res = coef * dot_prod
	res = round(res, 7)
	title = plt.title('Cost : ' + str(res))
	plt.getp(title)
	plt.show()

x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
# Example 1:
theta3 = np.array([12, 0.8])
plot_with_loss(x, y, theta3)
print(res)