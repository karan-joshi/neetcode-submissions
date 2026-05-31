"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.q = deque()
        self.node_map = {}
    
    def bfs(self):
        while self.q:
            node = self.q.popleft()
            copy = self.node_map[node]

            for child in node.neighbors:
                if child not in self.node_map:
                    child_copy = Node(child.val)
                    self.q.append(child)
                    self.node_map[child] = child_copy
                copy.neighbors.append(self.node_map[child])

                
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        head = Node(node.val)
        self.q.append(node)
        self.node_map[node] = head
        self.bfs()

        return head
        
