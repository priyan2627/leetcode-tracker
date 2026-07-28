# Last updated: 7/28/2026, 12:24:42 PM
1class Solution:
2    def isValid(self, s):
3        stack = []
4        mapping = {
5            ')': '(',
6            '}': '{',
7            ']': '['
8        }
9
10        for char in s:
11            if char in mapping:
12                if not stack or stack[-1] != mapping[char]:
13                    return False
14                stack.pop()
15            else:
16                stack.append(char)
17
18        return len(stack) == 0