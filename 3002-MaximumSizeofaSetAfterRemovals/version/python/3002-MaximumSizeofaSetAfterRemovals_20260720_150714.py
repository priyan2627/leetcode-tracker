# Last updated: 7/20/2026, 3:07:14 PM
1class Solution:
2    def maximumSetSize(self, nums1, nums2):
3        n = len(nums1)
4        limit = n // 2
5
6        s1 = set(nums1)
7        s2 = set(nums2)
8
9        only1 = len(s1 - s2)
10        only2 = len(s2 - s1)
11        common = len(s1 & s2)
12
13        take1 = min(only1, limit)
14        take2 = min(only2, limit)
15
16        remaining1 = limit - take1
17        remaining2 = limit - take2
18
19        return take1 + take2 + min(common, remaining1 + remaining2)