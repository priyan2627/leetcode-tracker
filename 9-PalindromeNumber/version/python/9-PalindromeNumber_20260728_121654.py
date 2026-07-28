# Last updated: 7/28/2026, 12:16:54 PM
1class Solution:
2    def threeSum(self, nums):
3        nums.sort()
4        result = []
5
6        for i in range(len(nums)):
7            # Skip duplicate elements
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10
11            left = i + 1
12            right = len(nums) - 1
13
14            while left < right:
15                total = nums[i] + nums[left] + nums[right]
16
17                if total == 0:
18                    result.append([nums[i], nums[left], nums[right]])
19
20                    # Skip duplicates
21                    while left < right and nums[left] == nums[left + 1]:
22                        left += 1
23                    while left < right and nums[right] == nums[right - 1]:
24                        right -= 1
25
26                    left += 1
27                    right -= 1
28
29                elif total < 0:
30                    left += 1
31                else:
32                    right -= 1
33
34        return result