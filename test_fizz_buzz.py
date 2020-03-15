import unittest 

from fizz_buzz_basic import fizz_buzz
from fizz_buzz_list import fizz_buzz_list
from fizz_buzz_state import fizz_buzz_state

class TestFizzBuzz(unittest.TestCase):
    print(
    """
    Testing Fizz Buzz as a list and a dictionary
    """
    )
    def test_list_1(self):
        print(
            """
            \n =================================\n
            testing a list of numbers from 0 to 4
            \n
            """
        )
        expected = ['FizzBuzz', 1, 2, 'Fizz', 4]
        actual = fizz_buzz_list(4)
        self.assertEqual(expected, actual)
    def test_list_2(self):
        print(
            """
            \n =================================\n
            testing an empty list
            \n
            """
        )
        expected = []
        actual = fizz_buzz_list(-1)
        self.assertEqual(expected, actual)

    def test_state_3(self):
        print(
            """
            \n =================================\n
            testing number 3
            \n
            """
        )
        expected = {0:'FizzBuzz', 1:1, 2:2, 3:'Fizz'}
        actual = fizz_buzz_state(3)
        self.assertEqual(expected, actual)

