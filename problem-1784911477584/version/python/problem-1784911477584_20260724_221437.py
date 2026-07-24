# Last updated: 7/24/2026, 10:14:37 PM
1
2class Solution:
3    def addTwoNumbers(self, l1, l2):
4        dummy = ListNode(0)
5        current = dummy
6        carry = 0
7
8        while l1 or l2 or carry:
9            x = l1.val if l1 else 0
10            y = l2.val if l2 else 0
11
12            total = x + y + carry
13            carry = total // 10
14
15            current.next = ListNode(total % 10)
16            current = current.next
17
18            if l1:
19                l1 = l1.next
20            if l2:
21                l2 = l2.next
22
23        return dummy.next