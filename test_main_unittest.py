import unittest
from main import sum
import difflib


class TestSumClass(unittest.TestCase):
	def test_sum_result(self):
		self.assertEqual(sum(7, 11), 18)


class _BaseTestCase(unittest.TestCase):
	def assertEqualWithDiff(self, a, b, msg=None):
		try:
			self._baseAssertEqual(a, b)
		except self.failureException:
			diff = difflib.unified_diff(
				a.splitlines(True),
				b.splitlines(True),
				n=0
			)
			diff = ''.join(diff)
			raise self.failureException("\n" + diff)


class MyTestCase(_BaseTestCase):
	def test_a(self):
		a = """hi
world
ok"""
		b = """hi
world
ok"""
# 		b = """bye
# world
# ok
# whatever"""
		self.assertEqualWithDiff(a, b)


if __name__ == '__main__':
	unittest.main()
