import unittest, random as rn
from linearSearch import linearSearch
from binarySearch import binarySearch
# linear search 12.456

class SearchingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = [i for i in range(0, 100000001)]
        self.n = rn.randint(0, 100000000)

    def test_linear(self):
        linear_search = linearSearch(self.arr, self.n)
        self.assertEqual(linear_search, self.n)
    def test_binary(self):
        binary_search = binarySearch(self.arr, self.n)
        self.assertEqual(binary_search, self.n)

if __name__ == '__main__':
    unittest.main()
