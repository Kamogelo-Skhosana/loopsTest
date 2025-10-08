import unittest
from loops import *
class TestLoops(unittest.TestCase):
    
    def test_count_items(self):
        self.assertEqual(count_items([1, 2, 3, 4, 5]), 5)
        self.assertEqual(count_items([]), 0)
        self.assertEqual(count_items(['a', 'b', 'c']), 3)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_find_largest(self):
        self.assertEqual(find_largest([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_largest([-5, -2, -10]), -2)
        self.assertEqual(find_largest([0]), 0)

    def test_count_even_numbers(self):
        self.assertEqual(count_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(count_even_numbers([1, 3, 5, 7, 9]), 0)
        self.assertEqual(count_even_numbers([2, 4, 6, 8]), 4)

    def test_sum_digits(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(9999), 36)
        self.assertEqual(sum_digits(1000000), 1)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_multiply_list_elements(self):
        self.assertEqual(multiply_list_elements([1, 2, 3, 4]), 24)
        self.assertEqual(multiply_list_elements([2, 2, 2]), 8)
        self.assertEqual(multiply_list_elements([1, 0, 5]), 0)


if __name__ == '__main__':
    unittest.main()