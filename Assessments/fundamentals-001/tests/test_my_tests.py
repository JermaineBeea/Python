import unittest
import test_assessment
import sys
import inspect
import io
import string_ops
import sequences
    


class TestMyTests(unittest.TestCase):

        def test_modules_exist(self):
            self.assertTrue('string_ops' in sys.modules, "string_ops module should be found")
            self.assertTrue('sequences' in sys.modules, "sequences module should be found")
            self.assertTrue('test_assessment' in sys.modules, "test_assessment module should be found")
    
        
        def test_number_of_tests(self):
            expected_minimum_tests = 7

           
            actual_number_of_tests = sum(1 for name in dir(test_assessment.MyTestClass) if name.startswith('test_'))

            self.assertGreaterEqual(actual_number_of_tests, expected_minimum_tests,
                                    f"Expected at least {expected_minimum_tests} tests, but found {actual_number_of_tests}.")
            

        
        def test_unittest_succeeds(self):

            suite = unittest.TestLoader().loadTestsFromTestCase(test_assessment.MyTestClass)

            test_result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)

            self.assertEqual(test_result.failures, [], "There should be no test failures")
            self.assertEqual(test_result.errors, [], "There should be no test errors")
            self.assertTrue(test_result.wasSuccessful(), "MyTestClass tests should succeed")
            
            
        def test_methods_are_not_empty(self):
            test_methods = [method for method in dir(test_assessment.MyTestClass) if method.startswith('test_')]
            for method in test_methods:
                method_obj = getattr(test_assessment.MyTestClass, method)
                source = inspect.getsource(method_obj)

            if 'pass' in source and len(source.strip().split('\n')) <= 2:
                self.fail(f"Method {method} is empty or contains only 'pass'")