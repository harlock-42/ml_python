import numpy as np

def check_ieter_type(iterable, type):
	return all(isinstance(val, type) for val in iterable)

class Matrix:
	def __init__tuple_(self, shape):
		# checking argument
		try:
			if len(shape) != 2:
				raise ValueError("Shape must has two arguments")
			if not check_ieter_type(shape, int):
				raise TypeError("Shape value must be integer")
			if not all(bool(val > 0) for val in shape):
				raise ValueError("Shape must have only positive values")
		except ValueError as ve:
			print("ValueError:", "Matrix:", ve)
		except TypeError as te:
			print("TypeError:", "Matrix", te)
		
		# set shape
		self.shape = shape

		# set data with a nested list filled by zero
		self.data = [[] for i in range(shape[1])]
		for nested_lst in self.data:
			for i in range(shape[0]):
				nested_lst.append(0.0)
		
	def __init__lst_(self, data):
		# checking argument
		try:
			if not check_ieter_type(data, list):
				raise TypeError("data must be a nested list")
			for lst in data:
				if not check_ieter_type(lst, float):
					raise TypeError("data must has only float values")
			if not all(bool(len(data[0]) == len(x)) for x in data):
				raise ValueError("All nested list of data have to be the same size")
		except TypeError as tp:
			print("TypeError:", "Matrix:", tp)
		except ValueError as ve:
			print("ValueError:", "Matrix:", ve)

		# set data
		self.data = data
		
		# set shape
		self.shape = (len((data[0])), len(data))

	def __str__(self):
		if type(self) == Vector:
			return 'Vector(' + str(self.data) + ')'
		return 'Matrix(' + str(self.data) + ')'

	def __repr__(self):
		if type(self) == Vector:
			return 'Vector(' + str(self.data) + ')'
		return 'Matrix(' + str(self.data) + ')'

	def __add__(self, other):
		try:
			if not isinstance(other, Matrix):
				raise TypeError("You have add a Matrix to another Matrix type")
			elif not check_ieter_type(other.data, list):
				raise TypeError("You have add a Matrix to another Matrix type")
			elif self.shape != other.shape:
				raise ValueError("The two matrix must be the same dimession")
		except ValueError as ve:
			print("ValueError:", "Matrix", ve)
			return None
		except TypeError as tp:
			print("TypeError:", "Matrix:", tp)
			return None
		res = self.data
		for j, row in enumerate(res):
			for i, nb in enumerate(row):
				res[j][i] += other.data[j][i]
		return res

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		try:
			if not isinstance(other, Matrix):
				raise TypeError("You have add a Matrix to another Matrix type")
			elif not check_ieter_type(other.data, list):
				raise TypeError("You have add a Matrix to another Matrix type")
			elif self.shape != other.shape:
				raise ValueError("The two matrix must be the same dimession")
		except ValueError as ve:
			print("ValueError:", "Matrix", ve)
			return None
		except TypeError as tp:
			print("TypeError:", "Matrix:", tp)
			return None
		res = self.data
		for j, row in enumerate(res):
			for i, nb in enumerate(row):
				res[j][i] -= other.data[j][i]
		return res

	def __rsub__(self, other):
		return self.__sub__(other)

	def __truediv__(self, other):
		try:
			if not isinstance(other, (int, float)):
				raise TypeError("Scalable must be an integer or float")
			if other == 0:
				raise ValueError("Scalable cannot be 0")
		except TypeError as te:
			print("TypeError:", "Matrix:", te)
			return None
		except ValueError as ve:
			print("TypeError:", "Matrix:", ve)
			return None
		res = self.data
		for j, row in enumerate(res):
			for i, nb in enumerate(row):
				res[j][i] /= other
		return res
	
	def __rtruediv__(self, other):
		print("ValueError: Matrix: a Matrix cannot be a divider")
		return None

	def get_col(self, i):
		return [lst[i] for lst in self.data]
	
	def get_prod(self, lst1, lst2):
		res = [0.0  for i in range(len(lst1))]
		for j in range(len(res)):
			res[j] = lst1[j] * lst2[j]
		return sum(res)

	def __mul__(self, other):
		try:
			if not isinstance(other, Matrix):
				raise TypeError("You can multiplicate only matrix with matrix")
			if self.shape[1] != other.shape[0]:
				raise ValueError("Shape matrix's product doesn't fit")
		except TypeError as tp:
			print("TypeError:", "Matrix:", tp)
			return None
		except ValueError as ve:
			print("ValueError:", "Matrix:", ve)
			return None
		res = [[self.get_prod(self.get_col(j), other.data[i]) for i in range(other.shape[1])] for j in range(self.shape[0])]
		return Matrix(res)

	def T(self):
		self.data = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
		self.shape = (len(self.data[0]), len(self.data))
	def __init__(self, args=None):
		if isinstance(args, tuple):
			self.__init__tuple_(args)
		elif isinstance(args, list):
			self.__init__lst_(args)

class Vector(Matrix):
	def __init__(self, arg):
		Matrix.__init__(self, arg)
		try:
			if self.shape[0] != 1 and self.shape[1] != 1:
				raise TypeError("data must have only one dimession")
		except TypeError as tp:
			print("TypeError:", "Vector:", tp)

	def dot(self, v):
		try:
			if self.shape[0] != len(v[0]) or self.shape[1] != len(v):
				raise TypeError("The two vector must have the same shape")
		except TypeError as tp:
			print("TypeError:", "Vector:", tp)
		res = [[i * v[0][x] for x, i in enumerate(j)] for j in self.data]
		return Vector(res)


m1 = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
m2 = Matrix([[2.0, 2.0, 2.0], [3.0, 3.0, 3.0], [10.0, 10.0, 10.0]])
v1 = Vector([[1.0, 2.0, 3.0]])
res = v1.dot([[2.0, 2.0, 2.0]])
print(res)
# print(v1)
res = m1 * m2
#check __add__ que ce soit bien deux Matrix
# print(res)














