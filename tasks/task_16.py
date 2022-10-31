"""2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 2**1000?"""


def get_exp_number(number: int, degree: int):
    return number ** degree


def get_sum_digit(number: int):
    return sum([int(i) for i in str(number)])


if __name__ == "__main__":
    assert get_exp_number(2, 15) == 32768
    assert get_sum_digit(32768) == 26

    exp_number = get_exp_number(2, 1_000)
    assert get_sum_digit(exp_number) == 1366
