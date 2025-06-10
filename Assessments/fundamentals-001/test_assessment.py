import unittest

import string_ops
import sequences


class MyTestClass(unittest.TestCase):


  def test_count_vowels(self):
    self.assertEqual(string_ops.count_vowels('abcdefghi'), 3)

  def test_reverse_word(self):
    self.assertEqual(string_ops.reverse_each_word('My name is David'), 'yM eman si divaD')

  def test_count_vowels_with_number(self):
    self.assertEqual(string_ops.count_vowels('12345'), 0)

  def test_count_vowels_with_empty(self):
    self.assertEqual(string_ops.count_vowels(''), 0)



  def test_generate_factorial(self):
    self.assertEqual(sequences.generate_factorial_series(5), [1, 2, 6, 24, 120])

  def test_generate_multiples(self):
    self.assertEqual(sequences.generate_multiples(6, 7), [7,14,21,28,35,42])
  
  def test_generate_factorial_zero(self):
    self.assertEqual(sequences.generate_factorial_series(0), [0])

  def test_multiples_zero(self):
    self.assertEqual(sequences.generate_multiples(6, 0), [0]* 6)

  def test_multiples_zero_2(self):
    self.assertEqual(sequences.generate_multiples(0, 7), [])

  def test_multiples_negative(self):
    self.assertEqual(sequences.generate_multiples(6, -3), [-3, -6, -9, -12, -15, -18])
    
