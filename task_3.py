import numpy as np

"""
The prime divisors of the number 13195 are 5, 7, 13 and 29.

What is the largest divisor of the number 600851475143, which is a prime number?
"""


def is_simple_number(number):
    if number in (2, 3):
        return True

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def simple_divisors(number):
    return [i for i in range(2, number // 2 + 1) if number % i == 0 and is_simple_number(i)]


def max_simple_divisor(number):
    for num in range(number // 2 + 1, 1, -1):
        if number % num == 0 and is_simple_number(num):
            return num
    return None


assert is_simple_number(1) == True
assert is_simple_number(2) == True
assert is_simple_number(3) == True
assert is_simple_number(4) == False
assert is_simple_number(5) == True
assert is_simple_number(7) == True
assert is_simple_number(13) == True
assert is_simple_number(25) == False
assert is_simple_number(29) == True

assert max_simple_divisor(13195) == 29
assert simple_divisors(13195) == [5, 7, 13, 29]
