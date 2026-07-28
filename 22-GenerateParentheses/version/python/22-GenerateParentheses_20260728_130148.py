# Last updated: 7/28/2026, 1:01:48 PM
1class Solution:
2    def removeElement(self, nums, val):
3        k = 0
4
5        for i in range(len(nums)):
6            if nums[i] != val:
7                nums[k] = nums[i]
8                k += 1
9
10        return k