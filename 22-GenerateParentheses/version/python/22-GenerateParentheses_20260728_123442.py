# Last updated: 7/28/2026, 12:34:42 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseKGroup(self, head, k):
9        dummy = ListNode(0)
10        dummy.next = head
11        group_prev = dummy
12
13        while True:
14            kth = group_prev
15
16            # Find the kth node
17            for _ in range(k):
18                kth = kth.next
19                if not kth:
20                    return dummy.next
21
22            group_next = kth.next
23
24            # Reverse the group
25            prev = group_next
26            curr = group_prev.next
27
28            while curr != group_next:
29                temp = curr.next
30                curr.next = prev
31                prev = curr
32                curr = temp
33
34            # Connect the reversed group
35            temp = group_prev.next
36            group_prev.next = kth
37            group_prev = temp