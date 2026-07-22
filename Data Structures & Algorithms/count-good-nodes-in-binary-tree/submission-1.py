# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(node,currmax):
            if not node:
                return
            currmax=max(currmax,node.val)
            if node.val>=currmax:
                nonlocal count
                count+=1
            dfs(node.left,currmax)
            dfs(node.right,currmax)
        dfs(root,root.val)
        return count

