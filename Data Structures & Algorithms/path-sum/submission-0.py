# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = self.dfs(root, targetSum, targetSum)
        return res

    def dfs(self, node, targetSum, remaining_val):
        if node is None:
            return False
        
        if node.left is None and node.right is None:
            print(remaining_val, node.val)
            return remaining_val == node.val
        
        remaining_val -= node.val

        return self.dfs(node.left, targetSum, remaining_val) or self.dfs(node.right, targetSum, remaining_val)
