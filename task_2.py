import numpy as np

"""Each next element of the Fibonacci series is obtained by adding the two previous ones.
Starting from 1 and 2, the first 10 elements will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all even elements of the Fibonacci series that do not exceed four million."""


def sum_fib(stop):
    seq = [1, 2]
    for i in range(3, stop + 1):
        if i == seq[-1] + seq[-2]:
            seq.append(i)

    seq = np.array(seq)
    return seq[seq % 2 == 0].sum()


assert sum_fib(89) == 44

print(sum_fib(4_000_000))
