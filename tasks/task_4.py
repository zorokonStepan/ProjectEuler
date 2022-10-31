import numpy as np

"""A palindrome number on both sides (from right to left and from left to right) reads the same.
The largest number is a palindrome obtained by multiplying two two-digit numbers – 9009 = 91 × 99.

Find the largest palindrome obtained by multiplying two three-digit numbers."""


def max_palindrome(start, stop):
    seq = np.array([i * j for i in range(start, stop) for j in range(start, stop) if str(i * j) == str(i * j)[::-1]])
    return seq.max()


if __name__ == "__main__":
    assert max_palindrome(10, 100) == 9009

    assert max_palindrome(100, 1000) == 906609
