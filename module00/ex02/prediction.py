import numpy as np

def simple_predict(x, theta):
	res = np.zeros(len(x))
	for i, nb in enumerate(x):
		res[i] = theta[0] + theta[1] * nb
	return res