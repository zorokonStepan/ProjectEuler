import numpy as np
from math import prod

"""2520 is the smallest number that is divisible without remainder by all numbers from 1 to 10.

What is the smallest number that is completely divisible by all numbers from 1 to 20?"""


def little_number(start, stop):
    seq = np.arange(start, stop + 1)
    max_num = prod(range(start, stop + 1))

    for num in range(stop, max_num + 1, stop):
        if not np.any(num % seq):
            return num
    return max_num


if __name__ == "__main__":
    assert little_number(1, 10) == 2520

    assert prod(range(1, 20 + 1)) == 2_432_902_008_176_640_000
    assert little_number(1, 20) == 232_792_560
