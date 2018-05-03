import unittest
from src.main import sum, square


class MyMathTest(unittest.TestCase):
	def test_sum_result(self):
		self.assertEqual(sum(1, 2), 3)

	def test_square_result(self):
		self.assertEqual(square(4), 16)

def test_sum_result_pytest():
	assert sum(1, 2) == 3

def test_square_result_pytest():
	assert square(4) == 16
