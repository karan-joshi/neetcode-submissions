class Solution:
    def __init__(self):
        self.visited = set()
        self.node_map = {}
    
    def dfs(self, node, parent):
        """helper method to check cycle"""
        if node in self.visited:
            return False

        self.visited.add(node)
        for child in self.node_map[node]:
            if child == parent:
                continue
            if not self.dfs(child, node):
                return False
        return True
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        self.node_map = {i: [] for i in range(n)}
        for node, child in edges:
            self.node_map[node].append(child)
            self.node_map[child].append(node)

        return self.dfs(0, -1) and len(self.visited) == n