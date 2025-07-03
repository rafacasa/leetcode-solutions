# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
            return head
        node = head.next.next
        even_start = head.next
        even_next = head.next
        head.next = node
        while node and node.next:
            even_next.next = node.next
            node.next = node.next.next
            node = node.next
            even_next = even_next.next
        node.next = even_start
        even_next.next = None

        return head


l1 = ListNode(
    2,
    ListNode(
        1,
        ListNode(
            4, ListNode(3, ListNode(6, ListNode(5, ListNode(7, ListNode(8, None)))))
        ),
    ),
)
ans = Solution().oddEvenList(l1)
while ans:
    print(ans.val)
    ans = ans.next
[2, 1, 4, 3, 6, 5, 7, 8]
