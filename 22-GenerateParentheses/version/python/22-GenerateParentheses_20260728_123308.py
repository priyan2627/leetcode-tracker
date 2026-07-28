# Last updated: 7/28/2026, 12:33:08 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def swapPairs(self, head):
9        dummy = ListNode(0)
10        dummy.next = head
11        prev = dummy
12
13        while prev.next and prev.next.next:
14            first = prev.next
15            second = first.next
16
17            # Swap
18            first.next = second.next
19            second.next = first
20            prev.next = second
21
22            # Move to the next pair
23            prev = first
24
25        return dummy.next