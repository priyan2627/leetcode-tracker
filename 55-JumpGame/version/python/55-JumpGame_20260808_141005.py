# Last updated: 8/8/2026, 2:10:05 PM
1class Solution:
2    def lengthOfLastWord(self, s):
3        s = s.strip()
4
5        count = 0
6
7        for i in range(len(s) - 1, -1, -1):
8            if s[i] == ' ':
9                break
10            count += 1
11
12        return count