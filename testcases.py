import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

# no, that would not have meant that the code was correct. The test cases did not test enough
# values to assess the functionality of the code. You only need to test one number, but the number
# must have the property n*n != 2n. so you just need to test another number that is not 2.
# it was not a syntax error, but a logical error made by the coder.