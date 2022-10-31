from math import sqrt, ceil


def is_simple_number(number: int):
    """
    1. все простые числа, за исключением двойки, нечётные.
    2. наименьший делитель составного числа N не превосходит sqrt(N)
    """
    if number == 2:
        return True

    if number % 2 == 0 or number < 2 or not isinstance(number, int):
        return False

    stop = ceil(sqrt(number)) + 1
    for i in range(3, stop, 2):
        if number % i == 0:
            return False
    return True


def test_is_simple_number():
    assert is_simple_number(2) is True
    assert is_simple_number(3) is True
    assert is_simple_number(5) is True
    assert is_simple_number(7) is True
    assert is_simple_number(13) is True
    assert is_simple_number(29) is True

    assert is_simple_number(1) is False
    assert is_simple_number(17.17) is False
    assert is_simple_number(4) is False
    assert is_simple_number(25) is False


def get_arr_simple_numbers(start: int, stop: int):
    return [i for i in range(start, stop) if is_simple_number(i)]


if __name__ == "__main__":
    test_is_simple_number()

    assert get_arr_simple_numbers(1, 100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                                              59, 61, 67, 71, 73, 79, 83, 89, 97]
