# Last updated: 7/28/2026, 12:10:20 PM
1class Solution:
2    def isPalindrome(self, x):
3        if x < 0:
4            return False
5
6        original = x
7        reverse = 0
8
9        while x > 0:
10            digit = x % 10
11            reverse = reverse * 10 + digit
12            x //= 10
13
14        return original == reverse