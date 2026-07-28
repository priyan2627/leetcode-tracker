# Last updated: 7/28/2026, 12:20:49 PM
1class Solution:
2    def letterCombinations(self, digits):
3        if not digits:
4            return []
5
6        phone = {
7            "2": "abc",
8            "3": "def",
9            "4": "ghi",
10            "5": "jkl",
11            "6": "mno",
12            "7": "pqrs",
13            "8": "tuv",
14            "9": "wxyz"
15        }
16
17        result = []
18
19        def backtrack(index, path):
20            if index == len(digits):
21                result.append(path)
22                return
23
24            for ch in phone[digits[index]]:
25                backtrack(index + 1, path + ch)
26
27        backtrack(0, "")
28        return result