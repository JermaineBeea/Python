import unittest
import test_assessment
import sys
import subprocess
import inspect
    


class TestMyTests(unittest.TestCase):

        def test_prime_numbers_sequences_modules_exist(self):
            self.assertTrue('prime_numbers' in sys.modules, "prime_numbers module should be found")
            self.assertTrue('sequences' in sys.modules, "sequences module should be found")

    
        def test_unittest_module_exist(self):
            self.assertTrue('test_assessment' in sys.modules, "test_assessment module should be found")
    
        
        def test_number_of_tests(self):
            expected_minimum_tests = 7

           
            actual_number_of_tests = sum(1 for name in dir(test_assessment.MyTestClass) if name.startswith('test_'))

            self.assertGreaterEqual(actual_number_of_tests, expected_minimum_tests,
                                    f"Expected at least {expected_minimum_tests} tests, but found {actual_number_of_tests}.")
            
        def test_unittest_succeeds(self):
           
            result = subprocess.run(['python', '-m', 'unittest', 'tests.test_assessment.MyTestClass'], capture_output=True)
            self.assertEqual(result.returncode, 0, "MyTestClass tests should succeed")
            
        def test_methods_are_not_empty(self):
            test_methods = [method for method in dir(test_assessment.MyTestClass) if method.startswith('test_')]
            for method in test_methods:
                method_obj = getattr(test_assessment.MyTestClass, method)
                source = inspect.getsource(method_obj)

            if 'pass' in source and len(source.strip().split('\n')) <= 2:
                self.fail(f"Method {method} is empty or contains only 'pass'")