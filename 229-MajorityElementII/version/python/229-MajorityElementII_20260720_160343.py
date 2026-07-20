# Last updated: 7/20/2026, 4:03:43 PM
1class Solution:
2    def maxTurbulenceSize(self, arr):
3        n = len(arr)
4
5        if n == 1:
6            return 1
7
8        up = 1
9        down = 1
10        ans = 1
11
12        for i in range(1, n):
13            if arr[i] > arr[i - 1]:
14                up = down + 1
15                down = 1
16            elif arr[i] < arr[i - 1]:
17                down = up + 1
18                up = 1
19            else:
20                up = down = 1
21
22            ans = max(ans, up, down)
23
24        return ans