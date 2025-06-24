# Accepted
# Runtime 53 ms Beats 48.65%
# Memory 23.85 MB Beats 29.94%


class Solution:

    def is_safe(self, node, curr_path):
        if len(self.graph) == 0:
            self.safe[node] = 1
            return True

        next_path = set(curr_path)
        next_path.add(node)
        for child in self.graph[node]:
            if child == node:
                self.safe[node] = 0
                return False
            if child in self.safe:
                if self.safe[child]:
                    continue
                self.safe[node] = 0
                return False
            if child in curr_path:
                self.safe[node] = 0
                return False
            if not self.is_safe(child, next_path):
                self.safe[node] = 0
                return False

        self.safe[node] = 1
        return True

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        self.graph = graph
        qtd_node = len(self.graph)
        self.safe = {}

        for i in range(qtd_node):
            if i not in self.safe:
                self.is_safe(i, {i})

        return sorted([node for node, status in self.safe.items() if status])
