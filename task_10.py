import numpy as np


"""
The sum of primes less than 10 is equal to 2 + 3 + 5 + 7 = 17.

Find the sum of all primes less than two million.
"""


def is_simple_number(number):
    if number in (2, 3):
        return True

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def sum_simple_numbers(func, stop):
    is_simple_number = np.vectorize(func)

    seq = np.arange(2, stop)
    return seq[is_simple_number(seq)].sum()


assert sum_simple_numbers(is_simple_number, 8) == 17

print(sum_simple_numbers(is_simple_number, 2_000_000)) # 142_913_828_922
