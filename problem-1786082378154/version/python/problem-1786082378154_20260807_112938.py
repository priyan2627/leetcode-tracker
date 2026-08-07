# Last updated: 8/7/2026, 11:29:38 AM
1class Solution:
2    def combinationSum2(self, candidates, target):
3        candidates.sort()
4        result = []
5
6        def backtrack(start, current, total):
7            if total == target:
8                result.append(current[:])
9                return
10
11            if total > target:
12                return
13
14            for i in range(start, len(candidates)):
15
16                # Skip duplicate values at the same level
17                if i > start and candidates[i] == candidates[i - 1]:
18                    continue
19
20                # Since array is sorted
21                if total + candidates[i] > target:
22                    break
23
24                current.append(candidates[i])
25
26                # i + 1 because each number can be used only once
27                backtrack(i + 1, current, total + candidates[i])
28
29                current.pop()
30
31        backtrack(0, [], 0)
32
33        return result