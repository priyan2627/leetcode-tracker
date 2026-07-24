# Last updated: 7/24/2026, 10:18:36 PM
1class Solution:
2    def longestPalindrome(self, s):
3        if len(s) < 2:
4            return s
5
6        start = 0
7        max_len = 1
8
9        for i in range(len(s)):
10
11            # Odd length palindrome
12            left = right = i
13            while left >= 0 and right < len(s) and s[left] == s[right]:
14                if right - left + 1 > max_len:
15                    start = left
16                    max_len = right - left + 1
17                left -= 1
18                right += 1
19
20            # Even length palindrome
21            left = i
22            right = i + 1
23            while left >= 0 and right < len(s) and s[left] == s[right]:
24                if right - left + 1 > max_len:
25                    start = left
26                    max_len = right - left + 1
27                left -= 1
28                right += 1
29
30        return s[start:start + max_len]