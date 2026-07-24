# Last updated: 7/24/2026, 10:17:21 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        if len(nums1) > len(nums2):
4            nums1, nums2 = nums2, nums1
5
6        m, n = len(nums1), len(nums2)
7        left, right = 0, m
8
9        while left <= right:
10            partitionX = (left + right) // 2
11            partitionY = (m + n + 1) // 2 - partitionX
12
13            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
14            minRightX = float('inf') if partitionX == m else nums1[partitionX]
15
16            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
17            minRightY = float('inf') if partitionY == n else nums2[partitionY]
18
19            if maxLeftX <= minRightY and maxLeftY <= minRightX:
20                if (m + n) % 2 == 0:
21                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
22                else:
23                    return max(maxLeftX, maxLeftY)
24
25            elif maxLeftX > minRightY:
26                right = partitionX - 1
27            else:
28                left = partitionX + 1