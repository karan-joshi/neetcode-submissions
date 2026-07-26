"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node_map = {}
        pointer = head

        while pointer:
            node_map[pointer] = Node(x = pointer.val)
            pointer = pointer.next

        for old, new in node_map.items():
            if old.next:
                new.next = node_map[old.next]
            if old.random:
                new.random = node_map[old.random]

        return node_map[head] if head else None
        