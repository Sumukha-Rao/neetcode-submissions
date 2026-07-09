# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0)
            left,left_not=dfs(node.left)
            right,right_not=dfs(node.right)
            rob=node.val+left_not+right_not
            rob_not=max(left,left_not)+max(right,right_not)
            return (rob,rob_not)
        return max(dfs(root))