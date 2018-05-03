def sum(a, b):
	"""This is the best thing in the world...

	>>> sum(1, 2)
	3
	>>> sum('a', 'b')
	'ab'
	>>> sum(-3, 9)
	6
	>>> sum('a', 4)
	Traceback (most recent call last):
	...
	TypeError: must be str, not int
	"""
	return a + b


if __name__ == '__main__':
		import doctest
		doctest.testmod()
