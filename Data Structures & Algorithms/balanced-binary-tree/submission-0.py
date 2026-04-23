# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root)
        if res == -1:
            return False
        return True

    def dfs(self, node):
        if node is None:
            return 0

        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)
        if left_depth == -1 or right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1