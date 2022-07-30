import numpy as np

"""
If we write out all natural numbers less than 10, multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these numbers is 23.

Find the sum of all numbers less than 1000, multiples of 3 or 5.
"""


def sum_num(start=1, stop=10):
    seq = np.arange(start, stop)
    return seq[(seq % 3 == 0) | (seq % 5 == 0)].sum()


assert sum_num(1, 10) == 23, 'The sum of natural numbers less than 10, multiples of 3 or 5 should be equal to 23'

sum_num(stop=1000)
