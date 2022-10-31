from math import sqrt

from utilites.simple_number import is_simple_number
"""
The prime divisors of the number 13195 are 5, 7, 13 and 29.

What is the largest divisor of the number 600851475143, which is a prime number?
"""


def simple_divisors(number):
    return [i for i in range(2, int(sqrt(number)) + 1) if number % i == 0 and is_simple_number(i)]


def max_simple_divisor(number):
    for num in range(int(sqrt(number)) + 1, 1, -1):
        if number % num == 0 and is_simple_number(num):
            return num
    return None


if __name__ == "__main__":
    assert max_simple_divisor(13195) == 29
    assert simple_divisors(13195) == [5, 7, 13, 29]

    assert max_simple_divisor(600851475143) == 6857
    assert simple_divisors(600851475143) == [71, 839, 1471, 6857]
