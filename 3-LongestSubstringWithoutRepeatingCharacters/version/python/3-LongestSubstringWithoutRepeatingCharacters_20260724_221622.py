# Last updated: 7/24/2026, 10:16:22 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s):
3        char_set = set()
4        left = 0
5        max_length = 0
6
7        for right in range(len(s)):
8            while s[right] in char_set:
9                char_set.remove(s[left])
10                left += 1
11
12            char_set.add(s[right])
13            max_length = max(max_length, right - left + 1)
14
15        return max_length