import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_generate_random_list(self):
        self.assertEqual(len(generate_random_list(10)), 10)
        self.assertEqual(len(generate_random_list(100)), 100)
        self.assertEqual(len(generate_random_list(1000)), 1000)

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-1, 2, -3, 4, -5, 6, -9, 10]), 10)
        self.assertEqual(find_max([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), 19)

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([-1, 2, -3, 4, -5, 6, -9, 10]), -9)
        self.assertEqual(find_min([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), -20)

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(find_average([-1, 2, -3, 4, -5, 6, -9, 10]), 0.5)
        self.assertEqual(find_average([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), -0.5)

    def test_find_even_pairs(self):
        self.assertEqual(find_even_pairs([1, 2, 3, 4, 5]), [])
        self.assertEqual(find_even_pairs([1, 2, 3, 4, 5, 6]), [])
        self.assertEqual(find_even_pairs([6, 2, 3, 5, 9, 4, 1, 11]), [(0, 1), (2, 3), (3, 4), (6, 7)])

    def test_find_odd_pairs(self):
        self.assertEqual(find_odd_pairs([1, 2, 3, 4, 5]), [(0, 1), (1, 2), (2, 3), (3, 4)])
        self.assertEqual(find_odd_pairs([1, 2, 3, 4, 5, 6]), [(0, 1),(1, 2), (2, 3),(3, 4), (4, 5)])
        self.assertEqual(find_odd_pairs([6, 2, 3, 5, 9, 4, 1, 11]), [(1, 2), (4, 5), (5, 6)])

    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5]), (2,4))
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5, 6]), (2,4,6))
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), (2,4,6,8))

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1,3,5))
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5, 6]), (1,3,5))
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8]), (1,3,5,7))

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_return_list_stats(self):
        self.assertEqual(return_list_stats([1, 2, 3, 4, 5]), {
            "unique_numbers": {1, 2, 3, 4, 5},
            "min": 1,
            "max": 5,
            "average": 3.0,
            "even_pairs": [],
            "odd_pairs": [(0, 1), (1, 2), (2, 3), (3, 4)],
            "even_numbers": (2, 4),
            "odd_numbers": (1, 3, 5),
            "number_of_even_numbers": 2,
            "number_of_odd_numbers": 3
        })
        self.assertEqual(return_list_stats([1, 2, 3, 4, 5, 6]), {
            "unique_numbers": {1, 2, 3, 4, 5, 6},
            "min": 1,
            "max": 6,
            "average": 3.5,
            "even_pairs": [],
            "odd_pairs": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
            "even_numbers": (2, 4, 6),
            "odd_numbers": (1, 3, 5),
            "number_of_even_numbers": 3,
            "number_of_odd_numbers": 3
        })
        self.assertEqual(return_list_stats([6, 2, 3, 5, 9, 4, 1, 11]), {
            "unique_numbers": {6, 2, 3, 5, 9, 4, 1, 11},
            "min": 1,
            "max": 11,
            "average": 5.1,
            "even_pairs": [(0, 1), (2, 3), (3, 4), (6, 7)],
            "odd_pairs": [(1, 2), (4, 5), (5, 6)],
            "even_numbers": (6, 2, 4),
            "odd_numbers": (3, 5, 9, 1, 11),
            "number_of_even_numbers": 3,
            "number_of_odd_numbers": 5
        })
