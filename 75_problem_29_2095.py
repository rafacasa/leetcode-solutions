# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_half = head
        cnt = 1
        node = head

        while node:
            if cnt > 2 and cnt % 2 == 0:
                pre_half = pre_half.next
            node = node.next
            cnt += 1

        if pre_half.next:
            pre_half.next = pre_half.next.next
        else:
            return None

        return head
