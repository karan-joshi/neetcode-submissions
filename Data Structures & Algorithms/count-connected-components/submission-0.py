class Solution:
    def __init__(self):
        self.node_map = {}
        self.visited = set()
    
    def dfs(self, node):
        if node in self.visited:
            return
        
        self.visited.add(node)

        for nei in self.node_map[node]:
            self.dfs(nei)

        return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.node_map = {i:[] for i in range(n)}
        for a, b in edges:
            self.node_map[a].append(b)
            self.node_map[b].append(a)

        count = 0
        for i in range(n):
            if i not in self.visited:
                self.dfs(i)
                count += 1

        return count