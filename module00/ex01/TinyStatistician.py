import numpy as np
import math

class TinyStatician:
	def __init__(self):
		pass
	
	def mean(self, x):
		res = 0.0
		for i in x:
			res += i
		return res / len(x)
	
	def median(self, x):
		x = sorted(x)
		return float(x[round(len(x) / 2)])

	def quartile(self, x):
		x = sorted(x)
		return ([float(x[math.trunc(len(x) / 4)]), float(x[math.trunc((len(x) / 4) * 3)])])

	def percentile(self, x, p):
		x = sorted(x)
		return (x[math.trunc((len(x) * p / 100))])
	
	def var(self, x):
		mean = self.mean(x)
		res = x
		for i, nb in enumerate(x):
			res[i] = float(pow(float(nb - mean), 2))
		return float(sum(res) / len(x))
	
	def std(self, x):
		return np.sqrt(self.var(x))