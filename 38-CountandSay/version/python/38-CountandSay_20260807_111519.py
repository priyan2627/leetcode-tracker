# Last updated: 8/7/2026, 11:15:19 AM
1class Solution:
2    def countAndSay(self, n):
3        result = "1"
4
5        for _ in range(n - 1):
6            next_result = ""
7            i = 0
8
9            while i < len(result):
10                count = 1
11
12                while i + 1 < len(result) and result[i] == result[i + 1]:
13                    count += 1
14                    i += 1
15
16                next_result += str(count) + result[i]
17                i += 1
18
19            result = next_result
20
21        return result