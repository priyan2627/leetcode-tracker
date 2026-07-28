# Last updated: 7/28/2026, 1:26:59 PM
1class Solution:
2    def searchRange(self, nums, target):
3        def findFirst():
4            left, right = 0, len(nums) - 1
5            first = -1
6
7            while left <= right:
8                mid = (left + right) // 2
9
10                if nums[mid] == target:
11                    first = mid
12                    right = mid - 1
13                elif nums[mid] < target:
14                    left = mid + 1
15                else:
16                    right = mid - 1
17
18            return first
19
20        def findLast():
21            left, right = 0, len(nums) - 1
22            last = -1
23
24            while left <= right:
25                mid = (left + right) // 2
26
27                if nums[mid] == target:
28                    last = mid
29                    left = mid + 1
30                elif nums[mid] < target:
31                    left = mid + 1
32                else:
33                    right = mid - 1
34
35            return last
36
37        return [findFirst(), findLast()]