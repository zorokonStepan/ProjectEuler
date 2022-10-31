from utilites.simple_number import is_simple_number

'''Writing out the first six primes, we get 2, 3, 5, 7, 11 and 13. Obviously, the 6th prime number is 13.

Which number is the 10001st prime number?'''

if __name__ == "__main__":
    num = 5
    lst_simple_numbers = [2, 3]

    while len(lst_simple_numbers) < 10_001:
        if is_simple_number(num):
            lst_simple_numbers.append(num)
        num += 2

    assert lst_simple_numbers[-1] == 104_743
    assert len(lst_simple_numbers) == 10_001
