# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            # leaf node identified
            self.res.append(node.val)
            return
        
        l = self.dfs(node.left)
        self.res.append(node.val)
        r = self.dfs(node.right)

        return