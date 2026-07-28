# Last updated: 7/28/2026, 12:23:31 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def removeNthFromEnd(self, head, n):
9        dummy = ListNode(0)
10        dummy.next = head
11
12        fast = dummy
13        slow = dummy
14
15        # Move fast pointer n+1 steps ahead
16        for _ in range(n + 1):
17            fast = fast.next
18
19        # Move both pointers
20        while fast:
21            fast = fast.next
22            slow = slow.next
23
24        # Remove the nth node
25        slow.next = slow.next.next
26
27        return dummy.next