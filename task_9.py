import numpy as np
import math

"""
The Pythagorean triple is three natural numbers a < b < c for which the equality holds

a ** 2 + b ** 2 = c ** 2
For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2.

There is only one Pythagorean triple for which a + b + c = 1000.
Find the work abc.
"""

result = [(i, j, k) for i in range(1, 1000 - 2)
                    for j in range(i + 1, 1000 - 1)
                    for k in range(j + 1, 1000)
                    if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2]

print(math.prod(result[0]))

assert result[0][0] + result[0][1] + result[0][2] == 1000
