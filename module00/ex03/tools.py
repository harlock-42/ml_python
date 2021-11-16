import numpy as np

def add_intercept(x):
	new_col = [1 for i in range(len(x))]
	return np.insert(x, 0, new_col, axis=1)