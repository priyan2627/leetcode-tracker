# Last updated: 7/28/2026, 12:22:09 PM
1class Solution:
2    def fourSum(self, nums, target):
3        nums.sort()
4        result = []
5        n = len(nums)
6
7        for i in range(n - 3):
8            # Skip duplicates for first number
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11
12            for j in range(i + 1, n - 2):
13                # Skip duplicates for second number
14                if j > i + 1 and nums[j] == nums[j - 1]:
15                    continue
16
17                left = j + 1
18                right = n - 1
19
20                while left < right:
21                    total = nums[i] + nums[j] + nums[left] + nums[right]
22
23                    if total == target:
24                        result.append([nums[i], nums[j], nums[left], nums[right]])
25
26                        # Skip duplicates
27                        while left < right and nums[left] == nums[left + 1]:
28                            left += 1
29                        while left < right and nums[right] == nums[right - 1]:
30                            right -= 1
31
32                        left += 1
33                        right -= 1
34
35                    elif total < target:
36                        left += 1
37                    else:
38                        right -= 1
39
40        return result