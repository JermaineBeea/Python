import unittest
from fundamentals import check_number

class MyTestCases (unittest.TestCase):

    """        
    test_check_number_odd_number: Tests for positive odd numbers.
    test_check_number_even_range_2_to_5: Tests for even numbers in the range 2 to 5, ensuring it returns "Not Weird".
    test_check_number_even_range_6_to_20: Tests for even numbers in the range 6 to 20, ensuring it returns "Weird".
    test_check_number_even_greater_than_20: Tests for even numbers greater than 20, ensuring it returns "Not Weird".
    test_check_number_negative_even_number: Tests for non-positive even numbers.
    test_check_number_negative_odd_number: Tests for non-positive odd numbers.
    test_check_number_neutral`: Tests for numbers that are neutral.

    """

    def test_check_number_even_number(self):
        self.assertTrue(check_number(2), True)

    def  test_check_number_odd_number(self):
        self.assertEqual(check_number(3), 'Weird')
    
    def  test_check_number_even_range_2_to_5(self):
        self.assertEqual(check_number(2), 'Not Weird')

    def  test_check_number_even_range_6_to_20(self):
        self.assertEqual(check_number(8), 'Weird')

    def  test_check_number_even_greater_than_20(self):
        self.assertEqual(check_number(22), 'Not Weird')

    def  test_check_number_negative_even_number(self):
        self.assertEqual(check_number(-2), 'Very Weird')

    def  test_check_number_negative_odd_number(self):
        self.assertEqual(check_number(-3), 'Weird')
    
    def test_check_number_neutral(self):
        self.assertEqual(check_number(0), 'Neutral')


if __name__ == '__main__':
    unittest.main()


