# Last updated: 7/9/2026, 10:21:49 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result