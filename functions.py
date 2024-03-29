from typing import Union

def divide(dividend: Union[int, float], divisor : Union[int, float]):
    if(divisor == 0):
        raise ValueError("The divisor cannot be zero.")
    return dividend / divisor

# Testing files for files to be tested should start with "test_".
# Testing file for this file should be "test_functions.py".

def multiply(*args : Union[int,float]):
    if( len(args) == 0):
        raise ValueError("At least one argument must be passed.")
    result = 1
    for value in args:
        result *= value
    return result
