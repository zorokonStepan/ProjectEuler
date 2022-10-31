from utilites.simple_number import is_simple_number

"""
The sum of primes less than 10 is equal to 2 + 3 + 5 + 7 = 17.
Find the sum of all primes less than two million.
"""


def sum_simple_numbers(stop):
    return sum([i for i in range(2, stop) if is_simple_number(i)])


if __name__ == "__main__":
    assert sum_simple_numbers(8) == 17
    assert sum_simple_numbers(2_000_000) == 142_913_828_922
