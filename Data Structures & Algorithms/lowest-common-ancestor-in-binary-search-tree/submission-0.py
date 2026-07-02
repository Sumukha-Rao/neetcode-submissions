# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor=root
        while ancestor:
            if (p.val<ancestor.val and q.val<ancestor.val):
                ancestor=ancestor.left
            elif (p.val>ancestor.val and q.val>ancestor.val):
                ancestor=ancestor.right
            else:
                return ancestor   
        
        