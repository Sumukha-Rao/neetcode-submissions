# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        d=defaultdict(list)
        def calcLevel(root,currlevel):
            if not root:
                return None
            d[currlevel].append(root.val)
            calcLevel(root.left,currlevel+1)
            calcLevel(root.right,currlevel+1)
        calcLevel(root,1)
        res=[]
        for i in d:
            res.append(d[i])
        return res