# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root, curr):
            nonlocal res
            if not root:
                res = max(curr, res)
                curr = 0
                return 
            curr += 1
            dfs(root.left, curr)
            dfs(root.right, curr)
        dfs(root, 0)
        print(res)
        return res