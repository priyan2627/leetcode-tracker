# Last updated: 7/28/2026, 1:12:06 PM
1class Solution:
2    def nextPermutation(self, nums):
3        n = len(nums)
4
5        # Step 1: Find the first decreasing element from the end
6        i = n - 2
7        while i >= 0 and nums[i] >= nums[i + 1]:
8            i -= 1
9
10        # Step 2: Find the next larger element and swap
11        if i >= 0:
12            j = n - 1
13            while nums[j] <= nums[i]:
14                j -= 1
15            nums[i], nums[j] = nums[j], nums[i]
16
17        # Step 3: Reverse the remaining part
18        left = i + 1
19        right = n - 1
20        while left < right:
21            nums[left], nums[right] = nums[right], nums[left]
22            left += 1
23            right -= 1