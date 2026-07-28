# Last updated: 7/28/2026, 12:19:16 PM
1class Solution:
2    def threeSumClosest(self, nums, target):
3        nums.sort()
4        closest = nums[0] + nums[1] + nums[2]
5
6        for i in range(len(nums) - 2):
7            left = i + 1
8            right = len(nums) - 1
9
10            while left < right:
11                total = nums[i] + nums[left] + nums[right]
12
13                if abs(target - total) < abs(target - closest):
14                    closest = total
15
16                if total < target:
17                    left += 1
18                elif total > target:
19                    right -= 1
20                else:
21                    return total
22
23        return closest