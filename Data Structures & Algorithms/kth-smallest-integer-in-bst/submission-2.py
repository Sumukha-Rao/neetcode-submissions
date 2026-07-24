# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=k
        def dfs(node):
            if not node:
                return None
            left=dfs(node.left)
            nonlocal count
            count-=1
            if count==0:
                return node.val
            right=dfs(node.right)
            return right if right else left
        return dfs(root)
