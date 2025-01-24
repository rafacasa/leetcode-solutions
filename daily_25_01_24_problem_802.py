# Accepted
# Runtime 1866 ms Beats 5.02%
# Memory 24.23 MB Beats 16.07%

class Solution:
    
    def is_safe(self, node, curr_path):
        if len(self.graph) == 0:
            self.safe.add(node)
            self.resolved.remove(node)
            return True
            
        next_path = (*curr_path, node)
        for child in self.graph[node]:
            if child == node:
                self.resolved.remove(node)
                self.not_safe.add(node)
                return False
            if child in self.safe:
                continue
            if child in self.not_safe:
                self.resolved.remove(node)
                self.not_safe.add(node)
                return False
            if child in curr_path:
                self.resolved.remove(node)
                self.not_safe.add(node)
                return False
            if not self.is_safe(child, next_path):
                self.resolved.remove(node)
                self.not_safe.add(node)
                return False
        
        self.resolved.remove(node)
        self.safe.add(node)
        return True
        
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.graph = graph
        qtd_node = len(self.graph)
        self.safe = set()
        self.not_safe = set()
        self.resolved = list(range(qtd_node))
        
        while self.resolved:
            self.is_safe(self.resolved[0], (self.resolved[0],))
        
        return sorted(self.safe)
