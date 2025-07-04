# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Accepted
# Runtime 83 ms Beats 46.15%
# Memory 41.38 MB Beats 82.22%


class Solution:
    def find_half(self, head):
        fast = slow = head
        while fast:
            slow = slow.next
            fast = fast.next.next
        return slow

    def invert_list(self, head):
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

    def pairSum(self, head: Optional[ListNode]) -> int:
        half_node = self.find_half(head)
        node2 = self.invert_list(half_node)
        node1 = head
        max_sum = float("-inf")

        while node1 and node2:
            max_sum = max(max_sum, node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next

        return max_sum
