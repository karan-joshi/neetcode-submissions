# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def invertRecursive(self, node: Optional[TreeNode]):
        if not node:
            return
        
        if node.left:
            self.invertRecursive(node.left)
        if node.right:
            self.invertRecursive(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

        return

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.invertRecursive(root)

        return root
        