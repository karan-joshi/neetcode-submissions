# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return True, float('inf'), float('-inf')
        
        left_cond, left_min, left_max = self.dfs(node.left)
        right_cond, right_min, right_max = self.dfs(node.right)

        curr_min = min(node.val, left_min, right_min)
        curr_max = max(node.val, left_max, right_max)
        if left_max >= node.val or right_min <= node.val:
            return False, curr_min, curr_max
        
        return left_cond and right_cond, curr_min, curr_max
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        valid, _, _ = self.dfs(root)

        return valid
        