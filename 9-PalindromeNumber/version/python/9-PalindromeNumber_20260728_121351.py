# Last updated: 7/28/2026, 12:13:51 PM
1class Solution:
2    def maxArea(self, height):
3        left = 0
4        right = len(height) - 1
5        max_water = 0
6
7        while left < right:
8            width = right - left
9            area = min(height[left], height[right]) * width
10            max_water = max(max_water, area)
11
12            if height[left] < height[right]:
13                left += 1
14            else:
15                right -= 1
16
17        return max_water