# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 19.34 MB Beats 29.54%


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = start of list
        # first_even = start of even members (starts on 2nd item)
        # last_odd = last odd member processed (starts on 1st item)
        # last_even = last even member processed (starts on 2nd item)
        # node = member being processed (starts on 3rd item)
        # Needs to filter lists with less than 3 itens

        # Filter empty lists
        if not head:
            return None

        # Filter list with size 1
        if not head.next:
            return head

        # Filter list with size 2
        if not head.next.next:
            return head

        first_even = head.next
        last_odd = head
        last_even = first_even
        node = last_even.next

        while node:
            # node is the next odd
            # node.next is the next even
            # node.next.next is the next node
            last_odd.next = node
            last_odd = node

            if node.next:
                # there is a next even item
                last_even.next = node.next
                last_even = node.next

                if node.next.next:
                    # there is a next node
                    node = node.next.next
                else:
                    node = None
            else:
                node = None
        last_odd.next = first_even
        last_even.next = None
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
