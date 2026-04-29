# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path = 0

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.max_path = max(self.max_path, left+right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.dfs(root)

        return self.max_path
        