# Last updated: 8/8/2026, 1:59:32 PM
1class Solution:
2    def merge(self, intervals):
3        if not intervals:
4            return []
5
6        intervals.sort(key=lambda x: x[0])
7
8        result = [intervals[0]]
9
10        for start, end in intervals[1:]:
11            last_end = result[-1][1]
12
13            
14            if start <= last_end:
15                result[-1][1] = max(last_end, end)
16
17            
18            else:
19                result.append([start, end])
20
21        return result