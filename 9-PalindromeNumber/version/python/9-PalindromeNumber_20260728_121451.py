# Last updated: 7/28/2026, 12:14:51 PM
1class Solution:
2    def intToRoman(self, num):
3        values = [
4            1000, 900, 500, 400,
5            100, 90, 50, 40,
6            10, 9, 5, 4, 1
7        ]
8
9        symbols = [
10            "M", "CM", "D", "CD",
11            "C", "XC", "L", "XL",
12            "X", "IX", "V", "IV", "I"
13        ]
14
15        result = ""
16
17        for i in range(len(values)):
18            while num >= values[i]:
19                result += symbols[i]
20                num -= values[i]
21
22        return result