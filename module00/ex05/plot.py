import matplotlib.pyplot as plt
import numpy as np

def plot(x, y, theta):
	fig = plt.figure()
	ax = plt.axes()
	# plt.scatter(x, y)
	x_min = x[0]
	x_max = x[len(x) - 1]
	y_min = x[0] * theta[1] + theta[0]
	y_max = x[len(x) -1] * theta[1] + theta[0]
	plt.plot([x_min, x_max], [y_min, y_max])
	plt.scatter(x, y)
	plt.show()