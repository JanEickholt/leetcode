import math
def isPowerOfFour(n):
    return math.log(n, 4).is_integer() if n > 0 else False
