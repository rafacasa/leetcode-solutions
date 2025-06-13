from collections import deque
from typing import List

# Accepted
# Runtime 17 ms Beats 41.72%
# Memory 24.97 MB Beats 5.25%
# NOT O(n) time complexity


class Solution_Sorted:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [str(i) for i in range(1, n + 1)]
        return sorted(ans)


# DFS Solution
# Accepted
# Runtime 183 ms Beats 5.00%
# Memory 23.95 MB Beats 17.06%


class Node:
    def __init__(self, num_str=None, num=None):
        if num_str:
            self.num_str = num_str
            self.num = int(num_str)
        else:
            self.num = num
            self.num_str = str(num)
        self.edges = []

    def generate_edges(self, limit):
        for digit in "9876543210":
            new_num = self.num_str + digit
            if int(new_num) <= limit:
                self.edges.append(Node(num_str=new_num))

    def dfs(self, limit):
        ans = []
        stack = deque()
        stack.append(self)

        while stack:
            node = stack.pop()
            ans.append(node.num)

            if not node.edges:
                node.generate_edges(limit)

            stack.extend(node.edges)

        return ans


class Solution_DFS:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for digit in range(1, 10):
            if digit <= n:
                start = Node(num=digit)
                ans.extend(start.dfs(n))
        return ans


# Recursive Solution
# Accepted
# Runtime 70 ms Beats 15.78%
# Memory 21.17 MB Beats 92.69%
class Solution_Recursive:
    def calculate(self, start, n):
        ans = [start]
        for i in range(10):
            num = 10 * start + i
            if 0 < num <= n:
                ans.extend(self.calculate(num, n))
        return ans

    def lexicalOrder(self, n: int) -> List[int]:
        return self.calculate(0, n)[1:]


# Solution from editorial
# Accepted
# Runtime 19 ms Beats 38.33%
# Memory 21.33 MB Beats 54.36%
class Solution_editorial:
    def generateNum(self, arr: List, num: int, limit: int) -> None:
        if num > limit:
            return
        arr.append(num)
        for d in range(10):
            next = 10 * num + d
            if next > limit:
                return
            self.generateNum(arr, next, limit)

    def lexicalOrder(self, n: int) -> List[int]:
        lex_num = []
        for i in range(1, 10):
            self.generateNum(lex_num, i, n)
        return lex_num


print(Solution_Sorted().lexicalOrder(13))
print(Solution_Sorted().lexicalOrder(2))
print(Solution_DFS().lexicalOrder(13))
print(Solution_DFS().lexicalOrder(2))
print(Solution_Recursive().lexicalOrder(13))
print(Solution_Recursive().lexicalOrder(2))
print(Solution_editorial().lexicalOrder(13))
print(Solution_editorial().lexicalOrder(2))
