try:
    from math import gcd
except ImportError:
    from fractions import gcd
from functools import reduce
print(reduce(gcd, [36, 12, 144, 18]))
