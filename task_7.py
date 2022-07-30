import numpy as np

'''Writing out the first six primes, we get 2, 3, 5, 7, 11 and 13. Obviously, the 6th prime number is 13.

Which number is the 10001st prime number?'''


def is_simple_number(number):
    if number in (2, 3):
        return True

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


cnt = 2
num = 5
lst_simple_numbers = [2, 3]

while cnt < 10_001:
    if is_simple_number(num):
        lst_simple_numbers.append(num)
        cnt += 1
    num += 1

print(len(lst_simple_numbers), lst_simple_numbers[-1])  # 10001 104743
