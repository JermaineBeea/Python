import unittest
from unittest import mock
from io import StringIO
from functions_exercise.functions_exercise2 import *


class TestUserInputFunctions(unittest.TestCase):
    def test_get_user_input(self):
        # Mocking user input for testing
        inputs = ["JohnDoe", "25", "john.doe@example.com"]

        with unittest.mock.patch('builtins.input', side_effect=inputs):
            result = get_user_input()
            self.assertEqual(result, ("JohnDoe", 25, "john.doe@example.com"))

    def test_wrong_age_input(self):
        # Mocking user input for testing
        inputs = ["JohnDoe", "twenty", 25, "john.doe@example.com"]

        with mock.patch('builtins.input', side_effect=inputs):
            with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = get_user_input()
                self.assertEqual(result, ("JohnDoe", 25, "john.doe@example.com"))

                # Check if the correct message is printed when an invalid age is entered
                expected_output = "Not an Integer, Enter a valid age!\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_valid_username(self):
        result = validate_username("JohnDoe")
        self.assertTrue(result)

    def test_empty_username(self):
        result = validate_username("")
        self.assertFalse(result)

    def test_invalid_username(self):
        result = validate_username("John123")
        self.assertFalse(result)

    def test_display_user_info_output(self, mock_stdout):
        result = display_user_info("JohnDoe", 25, "john.doe@example.com")
        expected_output = "\nUser Information:\nUsername : JohnDoe\nAge      : 25\nEmail    : john.doe@example.com"
        self.assertEqual(result, 'Thanks!, Details captured.')
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_display_user_info_return(self):
        result = display_user_info("JohnDoe", 25, "john.doe@example.com")
        self.assertEqual(result, 'Thanks!, Details captured.')

if __name__ == "__main__":
    unittest.main()
