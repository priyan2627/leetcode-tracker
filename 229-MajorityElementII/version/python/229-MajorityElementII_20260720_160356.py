# Last updated: 7/20/2026, 4:03:56 PM
1class Solution:
2    def majorityElement(self, nums):
3        candidate1 = None
4        candidate2 = None
5        count1 = 0
6        count2 = 0
7
8        # Find potential candidates
9        for num in nums:
10            if candidate1 == num:
11                count1 += 1
12            elif candidate2 == num:
13                count2 += 1
14            elif count1 == 0:
15                candidate1 = num
16                count1 = 1
17            elif count2 == 0:
18                candidate2 = num
19                count2 = 1
20            else:
21                count1 -= 1
22                count2 -= 1
23
24        # Verify the candidates
25        count1 = 0
26        count2 = 0
27
28        for num in nums:
29            if num == candidate1:
30                count1 += 1
31            elif num == candidate2:
32                count2 += 1
33
34        result = []
35
36        if count1 > len(nums) // 3:
37            result.append(candidate1)
38
39        if count2 > len(nums) // 3:
40            result.append(candidate2)
41
42        return result