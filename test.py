"""This program is to determine the math function copysign"""
import unittest
# from wrapper_copysign import wrapper

class TestCopysignMethod(unittest.TestCase):
    """"This class has methods which check the validity of arguments for
    the copysign wrapper"""

    def test_wrapper_correct_arguments(self):
        """This function checks if the arguments are of valid types"""
        self.assertEqual(wrapper(1.79), 2)

    def test_wrapper_incorrect_args(self):
        """This function checks if the arguments are of valid types"""
        with self.assertRaises(TypeError):
            wrapper(1)

    def test_wrapper_no_args(self):
        """This function checks if the arguments are of valid types"""
        with self.assertRaises(TypeError):
            wrapper()


if __name__ == '__main__':
    unittest.main()
