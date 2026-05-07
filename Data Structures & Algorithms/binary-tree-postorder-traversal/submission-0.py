# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None:
            return
        
        self.dfs(node.left)
        self.dfs(node.right)

        self.res.append(node.val)
        return