# Last updated: 7/28/2026, 12:08:56 PM
1class Solution:
2    def myAtoi(self, s):
3        i = 0
4        n = len(s)
5
6        # Skip leading spaces
7        while i < n and s[i] == ' ':
8            i += 1
9
10        # Check if string is empty after spaces
11        if i == n:
12            return 0
13
14        # Check sign
15        sign = 1
16        if s[i] == '-':
17            sign = -1
18            i += 1
19        elif s[i] == '+':
20            i += 1
21
22        # Convert digits
23        result = 0
24        while i < n and s[i].isdigit():
25            result = result * 10 + int(s[i])
26            i += 1
27
28        result *= sign
29
30        # Clamp to 32-bit integer range
31        INT_MIN = -2**31
32        INT_MAX = 2**31 - 1
33
34        if result < INT_MIN:
35            return INT_MIN
36        if result > INT_MAX:
37            return INT_MAX
38
39        return result