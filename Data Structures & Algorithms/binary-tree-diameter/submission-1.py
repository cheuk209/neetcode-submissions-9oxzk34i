# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        res = self.dfs(root)
        return self.max_len

    def dfs(self, node) -> int:
        if node == None:
            return 0
        
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        curr_len = l + r
        self.max_len = max(self.max_len, curr_len)

        return max(l, r) + 1