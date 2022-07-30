import numpy as np

'''
A sequence of triangular numbers is formed by adding natural numbers.
For example, the 7th triangular number is 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten triangular numbers:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let 's list the divisors of the first seven triangular numbers:

1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
As we can see, 28 is the first triangular number with more than five divisors.

What is the first triangular number that has more than five hundred divisors?
'''


class MyNumbers:

    """infinite sequence of natural numbers"""

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        x = self.n
        self.n += 1
        return x


def count_divisors(number: int):
    if number in (1, -1):
        return 1
    if number == 0:
        return None
    if number in (2, 3, -2, -3):
        return 2

    cnt_divisors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            cnt_divisors.append(i)
    cnt_divisors.append(number)

    return len(cnt_divisors)


assert count_divisors(1) == 1
assert count_divisors(3) == 2
assert count_divisors(6) == 4
assert count_divisors(10) == 4
assert count_divisors(15) == 4
assert count_divisors(21) == 4
assert count_divisors(28) == 6


def triangular_number_with_a_certain_number_of_divisors(stop: int):
    triangular_number = 1
    number = MyNumbers()
    myiter = iter(number)
    next(myiter)

    cnt_div = count_divisors(triangular_number)

    while cnt_div < stop:
        triangular_number += next(myiter)
        cnt_div = count_divisors(triangular_number)

    if cnt_div == stop:
        return triangular_number
    else:
        return None


assert triangular_number_with_a_certain_number_of_divisors(1) == 1
assert triangular_number_with_a_certain_number_of_divisors(2) == 3
assert triangular_number_with_a_certain_number_of_divisors(3) == None
assert triangular_number_with_a_certain_number_of_divisors(4) == 6
assert triangular_number_with_a_certain_number_of_divisors(5) == None
assert triangular_number_with_a_certain_number_of_divisors(6) == 28


def is_triangular_number(number: int):
    num = MyNumbers()
    myiter = iter(num)

    while number > 0:
        number -= next(myiter)

    if number == 0:
        return True
    return False


assert is_triangular_number(1) == True
assert is_triangular_number(3) == True
assert is_triangular_number(6) == True
assert is_triangular_number(10) == True
assert is_triangular_number(15) == True
assert is_triangular_number(21) == True
assert is_triangular_number(28) == True
