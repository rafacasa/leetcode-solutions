# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 18.02 MB Beats 5.03%


class Solution:
    def find_leaf_value(self, root: Optional[TreeNode]) -> list:
        stack = deque()
        stack.append(root)
        ans = list()

        while stack:
            item = stack.pop()
            if (not item.left) and (not item.right):
                ans.append(item.val)
                continue
            if item.left:
                stack.append(item.left)
            if item.right:
                stack.append(item.right)
        return ans

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = self.find_leaf_value(root1)
        l2 = self.find_leaf_value(root2)

        if len(l1) != len(l2):
            return False

        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False

        return True
