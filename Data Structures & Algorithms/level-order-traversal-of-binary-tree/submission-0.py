# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
            
        res = []
        queue = []
        queue.append(root)

        while queue:
            level = []
            values = []
            for node in queue:
                values.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            queue = level
            res.append(values)

        return res