# Last updated: 7/24/2026, 10:20:15 PM
1class Solution:
2    def convert(self, s, numRows):
3        if numRows == 1 or numRows >= len(s):
4            return s
5
6        rows = [""] * numRows
7        current_row = 0
8        direction = -1
9
10        for char in s:
11            rows[current_row] += char
12
13            if current_row == 0 or current_row == numRows - 1:
14                direction *= -1
15
16            current_row += direction
17
18        return "".join(rows)