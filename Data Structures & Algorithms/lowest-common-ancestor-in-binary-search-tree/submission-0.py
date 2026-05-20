# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr_node = root
        lca = None

        # swap p and q such that p.val <= q.val
        if p.val >= q.val:
            temp = p
            p = q
            q = temp

        while curr_node:
            if curr_node.val == p.val or curr_node.val == q.val:
                lca = curr_node
                break
            elif p.val < curr_node.val < q.val:
                lca = curr_node
                break
            elif p.val < curr_node.val and q.val < curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return lca
            