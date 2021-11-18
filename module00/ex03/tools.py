import numpy as np

def add_intercept(x):
	new_col = [1 for i in range(len(x))]
	New_col = np.array(new_col)
	return np.c_[New_col, x]