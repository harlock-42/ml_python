import numpy as np

"""
  Description:
    Calculate the MSE between the predicted output and the real output.
  Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
  Returns:
    mse: has to be a float.
    None if there is a matching shape problem.
  Raises:
    This function should not raise any Exception.
"""

def mean_squared_error(y, y_hat):
	if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
		return None
	if y.shape != y_hat.shape:
		return None
	if y.size == 0 or y_hat.size == 0:
		return None
	return 1 / len(y) * (sum((y_hat - y) ** 2))

"""
  Description:
    Calculate the RMSE between the predicted output and the real output.
  Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
  Returns:
    rmse: has to be a float.
    None if there is a matching shape problem.
  Raises:
    This function should not raise any Exception.
"""

def rmse_(y, y_hat):
	if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
		return None
	if y.shape != y_hat.shape:
		return None
	if y.size == 0 or y_hat.size == 0:
		return None
	return np.sqrt(1 / len(y) * (sum((y_hat - y) ** 2)))

"""
  Description:
    Calculate the MAE between the predicted output and the real output.
  Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
  Returns:
    mae: has to be a float.
    None if there is a matching shape problem.
  Raises:
    This function should not raise any Exception.
"""

def mae_(y, y_hat):
	if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
		return None
	if y.shape != y_hat.shape:
		return None
	if y.size == 0 or y_hat.size == 0:
		return None
	res = sum(np.sqrt((y_hat - y) ** 2))
	res = (1 / len(y)) * res
	return res

"""
  Description:
    Calculate the R2score between the predicted output and the output.
  Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
  Returns:
    r2score: has to be a float.
    None if there is a matching shape problem.
  Raises:
    This function should not raise any Exception.
"""

def r2score_(y, y_hat):
	if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
		return None
	if y.shape != y_hat.shape:
		return None
	if y.size == 0 or y_hat.size == 0:
		return None
	return 1.0 - (sum((y_hat - y) ** 2) / sum((y - np.mean(y_hat)) ** 2))