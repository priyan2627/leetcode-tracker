# Last updated: 7/28/2026, 1:10:01 PM
1class Solution:
2    def divide(self, dividend, divisor):
3        INT_MAX = 2**31 - 1
4        INT_MIN = -2**31
5
6        # Overflow case
7        if dividend == INT_MIN and divisor == -1:
8            return INT_MAX
9
10        # Determine sign
11        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
12
13        dividend = abs(dividend)
14        divisor = abs(divisor)
15
16        quotient = 0
17
18        while dividend >= divisor:
19            temp = divisor
20            multiple = 1
21
22            while dividend >= (temp << 1):
23                temp <<= 1
24                multiple <<= 1
25
26            dividend -= temp
27            quotient += multiple
28
29        return sign * quotient