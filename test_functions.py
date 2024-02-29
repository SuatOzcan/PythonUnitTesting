from unittest import TestCase
from functions import *

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
    
    def test_divide_dividend_zero(self):
        dividend =0
        divisor =3
        expected_result = 0
        self.assertEqual(divide(dividend,divisor),expected_result)
    
    def test_divide_error_on_divisor_zero(self):
        self.assertRaises(ValueError,lambda:divide(15,0))
        # Or
        with self.assertRaises(ValueError):
            divide(15,0)
    
    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()
    
    def test_multiply_single_value(self):
        expected_result = 15
        self.assertAlmostEqual(multiply(15),expected_result,delta=0.0001)


    def test_multiply_with_zero(self):
        expected_result = 0
        self.assertEqual(multiply(0),expected_result)

    def test_multiply_result(self):
        inputs = (1,2,15)
        expected_result = 30
        self.assertAlmostEqual(multiply(*inputs),expected_result,delta=0.0001)
    
    def test_multiply_result_with_zero(self):
        inputs =(1,2,3,4,5,0)
        expected_result = 0
        self.assertAlmostEqual(multiply(*inputs),expected_result,delta=0.0001)    
    
    def test_multiply_negative_values(self):
        inputs=(1,2,3,4,5,-5)
        expected_result =-600
        self.assertAlmostEqual(multiply(*inputs),expected_result,delta=0.0001)
    
    def test_multiply_negative_values_zero(self):
        inputs = (1,2,3,4,0)
        expected_result = 0
        self.assertAlmostEqual(multiply(*inputs),expected_result,delta=0.0001)



# Now type in the console python -m unittest test_functions.py

# If we run the code below, it will raise an exception
# if the expected value and the return of the function are not equal.
test_function = TestFunctions()
print(test_function.test_divide_result())

