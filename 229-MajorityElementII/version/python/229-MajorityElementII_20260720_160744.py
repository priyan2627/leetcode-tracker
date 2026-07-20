# Last updated: 7/20/2026, 4:07:44 PM
1class Solution:
2    def rotate(self, matrix):
3        n = len(matrix)
4
5        # Step 1: Transpose
6        for i in range(n):
7            for j in range(i + 1, n):
8                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
9
10        # Step 2: Reverse each row
11        for row in matrix:
12            row.reverse()