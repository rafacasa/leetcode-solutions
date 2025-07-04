# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 19.01 MB Beats 5.36%


class Solution:
    def invert(self, prev: Optional[ListNode], node: Optional[ListNode]):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return self.invert(node, next)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        node = head.next
        head.next = None
        return self.invert(head, node)


# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 18.89 MB Beats 14.68%


class Solution_iter:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        node = head.next
        head.next = None
        prev = head

        while node:
            next = node.next
            node.next = prev
            prev = node
            if not next:
                return node
            node = next
