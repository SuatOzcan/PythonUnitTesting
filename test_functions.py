from unittest import TestCase
from functions import divide

class TestFunctions(TestCase):
    # Functions should also start with "test_".
    def test_divide_result(self):
        dividend = 15
        divisor =3
        expected_result = 5.0
       # self.assertEqual(divide(dividend,divisor),expected_result,
        #                 msg="The expected result and the return of the function are not equal.")
        # The line above is the real way, but because we are using floats,
        # choosing the .assertAlmostEqual method is the viable option.
        self.assertAlmostEqual(divide(dividend,divisor),expected_result,
                         msg="The expected result and the return of the function are not equal.",
                        delta = 0.0001)

    def test_divide_negative_result(self):
        dividend = 15
        divisor = -3
        expected_result = -5
        self.assertAlmostEqual(divide(dividend,divisor),expected_result,delta=0.0001)
# Now type in the console python -m unittest test_functions.py

# If we run the code below, it will raise an exception
# if the expected value and the return of the function are not equal.
test_function = TestFunctions()
print(test_function.test_divide_result())

