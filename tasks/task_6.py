import numpy as np

"""
The sum of the squares of the first ten natural numbers is

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is

(1 + 2 + ... + 10)2 = 55**2 = 3025
Therefore, the difference between the sum of squares and the square of the sum of the first ten natural numbers
is 3025 − 385 = 2640.

Find the difference between the sum of squares and the square of the sum of the first hundred natural numbers.
"""


def diff_sum_squares_and_square_sum(start, stop):
    seq = np.arange(start, stop + 1)
    sum_squares = sum([i ** 2 for i in seq])
    square_sum = seq.sum() ** 2
    return square_sum - sum_squares


if __name__ == "__main__":
    assert diff_sum_squares_and_square_sum(1, 10) == 2640

    assert diff_sum_squares_and_square_sum(1, 100) == 25164150
