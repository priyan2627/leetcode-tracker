# Last updated: 7/28/2026, 1:04:06 PM
1class Solution:
2    def strStr(self, haystack, needle):
3        n = len(haystack)
4        m = len(needle)
5
6        for i in range(n - m + 1):
7            if haystack[i:i + m] == needle:
8                return i
9
10        return -1