import numpy as np
import math

"""2520 is the smallest number that is divisible without remainder by all numbers from 1 to 10.

What is the smallest number that is completely divisible by all numbers from 1 to 20?"""


def little_number(start, stop):
    seq = np.arange(start, stop + 1)
    max_num = math.prod(seq)
    num = stop + 1
    while True:
        if not np.any(num % seq):
            return num
        num += 1

        if num > max_num:
            return None


assert little_number(1, 10) == 2520
