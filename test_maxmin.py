import unittest
from maxmin import max_min_select

class TestMaxMin(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(max_min_select([1, 2, 3, 4, 5]), (5, 1))

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            max_min_select([])

    def test_single_element_array(self):
        self.assertEqual(max_min_select([42]), (42, 42))

    def test_two_elements_array(self):
        self.assertEqual(max_min_select([2, 1]), (2, 1))
        self.assertEqual(max_min_select([1, 2]), (2, 1))

    def test_negative_numbers(self):
        self.assertEqual(max_min_select([-1, -2, -3, -4, -5]), (-1, -5))

    def test_duplicate_elements(self):
        self.assertEqual(max_min_select([2, 2, 2, 2, 2]), (2, 2))

    def test_large_array(self):
        large_array = list(range(1000))
        self.assertEqual(max_min_select(large_array), (999, 0))

if __name__ == '__main__':
    unittest.main()