# Last updated: 7/28/2026, 12:30:47 PM
1import heapq
2
3# Definition for singly-linked list.
4# class ListNode:
5#     def __init__(self, val=0, next=None):
6#         self.val = val
7#         self.next = next
8
9class Solution:
10    def mergeKLists(self, lists):
11        heap = []
12
13        # Add the first node of each list to the heap
14        for i, node in enumerate(lists):
15            if node:
16                heapq.heappush(heap, (node.val, i, node))
17
18        dummy = ListNode(0)
19        current = dummy
20
21        while heap:
22            val, i, node = heapq.heappop(heap)
23
24            current.next = node
25            current = current.next
26
27            if node.next:
28                heapq.heappush(heap, (node.next.val, i, node.next))
29
30        return dummy.next