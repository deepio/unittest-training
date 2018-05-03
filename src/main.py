def sum(a, b):
	"""
	This is AMAZING!!!
	>>> sum(3,5)
	8
	>>> sum(7,15)
	22
	>>> sum('a', 4)
	Traceback (most recent call last):
	...
	TypeError: must be str, not int
	"""
	return a + b


def square(a):
	"""
	This is AMAZING!!!
	>>> square(3)
	9
	"""
	return a**2


if __name__ == '__main__':
		import doctest
		doctest.testmod()

