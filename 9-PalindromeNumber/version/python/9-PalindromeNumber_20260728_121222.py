# Last updated: 7/28/2026, 12:12:22 PM
1class Solution:
2    def isMatch(self, s, p):
3        m, n = len(s), len(p)
4
5        dp = [[False] * (n + 1) for _ in range(m + 1)]
6        dp[0][0] = True
7
8        # Handle patterns like a*, a*b*, etc.
9        for j in range(2, n + 1):
10            if p[j - 1] == '*':
11                dp[0][j] = dp[0][j - 2]
12
13        for i in range(1, m + 1):
14            for j in range(1, n + 1):
15                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
16                    dp[i][j] = dp[i - 1][j - 1]
17
18                elif p[j - 1] == '*':
19                    # Zero occurrences
20                    dp[i][j] = dp[i][j - 2]
21
22                    # One or more occurrences
23                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
24                        dp[i][j] = dp[i][j] or dp[i - 1][j]
25
26        return dp[m][n]