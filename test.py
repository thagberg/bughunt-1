import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_three(self):
        result = fizzbuzz.fb_test(3)
        self.assertEqual(result, "Fizz")

    def test_five(self):
        result = fizzbuzz.fb_test(5)
        self.assertEqual(result, "Buzz")

    def test_fifteen(self):
        result = fizzbuzz.fb_test(15)
        self.assertEqual(result, "FizzBuzz")

    def test_sevent(self):
        result = fizzbuzz.fb_test(7)
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()