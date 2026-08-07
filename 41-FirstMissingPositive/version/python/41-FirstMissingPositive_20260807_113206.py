# Last updated: 8/7/2026, 11:32:06 AM
1class Solution:
2    def firstMissingPositive(self, nums):
3        n = len(nums)
4
5        # Put each number in its correct position
6        for i in range(n):
7            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
8                correct_index = nums[i] - 1
9                nums[i], nums[correct_index] = nums[correct_index], nums[i]
10
11        # Find the first position with the wrong number
12        for i in range(n):
13            if nums[i] != i + 1:
14                return i + 1
15
16        # If all 1 to n are present
17        return n + 1