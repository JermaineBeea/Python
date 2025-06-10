import unittest
from unittest.mock import patch
from functions_exercise.functions_exercise import *
from io import StringIO

class TestFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_add_positive_and_negative_numbers(self):
        result = add_numbers(5, -3)
        self.assertEqual(result, 2)

    def test_add_zero_to_positive_number(self):
        result = add_numbers(0, 7)
        self.assertEqual(result, 7)

    def test_add_zero_to_negative_number(self):
        result = add_numbers(0, -5)
        self.assertEqual(result, -5)

    def test_add_zero_to_zero(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

    def test_calculate_sum(self):
        result = calculate_sum([1, 2, 3])
        self.assertEqual(result, 6)

    def test_demonstrate_scoping(self):
        # Redirect stdout to capture print statements
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            demonstrate_scoping()
            expected_output = "Global variable: I am a global variable\nLocal variable: I am a local variable\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('your_module_name.rectangle_area', return_value=15)  # Example: length=5, width=3
    @patch('your_module_name.circle_area', return_value=50.26548245743669)  # Example: radius=4
    def test_calculate_area_with_valid_inputs(self, mock_rectangle_area, mock_circle_area):
        result = calculate_area(5, 3, 4)
        mock_rectangle_area.assert_called_with(5, 3)
        mock_circle_area.assert_called_with(4)
        self.assertEqual(result, (15, 50.26548245743669))

    @patch('your_module_name.rectangle_area', return_value=0)
    @patch('your_module_name.circle_area', return_value=0)
    def test_calculate_area_with_zero_inputs(self, mock_rectangle_area, mock_circle_area):
        result = calculate_area(0, 0, 0)
        mock_rectangle_area.assert_called_with(0, 0)
        mock_circle_area.assert_called_with(0)
        self.assertEqual(result, (0, 0))

    @patch('your_module_name.rectangle_area', return_value=100)
    @patch('your_module_name.circle_area', return_value=0)
    def test_calculate_area_with_only_rectangle(self, mock_rectangle_area, mock_circle_area):
        result = calculate_area(10, 10, 0)
        mock_rectangle_area.assert_called_with(10, 10)
        mock_circle_area.assert_not_called()
        self.assertEqual(result, (100, 0))

    @patch('your_module_name.rectangle_area', return_value=0)
    @patch('your_module_name.circle_area', return_value=12.566370614359172)  
    def test_calculate_area_with_only_circle(self, mock_rectangle_area, mock_circle_area):
        result = calculate_area(0, 0, 2)
        mock_rectangle_area.assert_not_called()
        mock_circle_area.assert_called_with(2)
        self.assertEqual(result, (0, 12.566370614359172))

if __name__ == "__main__":
    unittest.main()
