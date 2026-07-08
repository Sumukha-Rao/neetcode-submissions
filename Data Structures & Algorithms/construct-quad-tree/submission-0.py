"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,row,column):
            allSame=True
            for i in range(n):
                for j in range(n):
                    if grid[row][column]!=grid[row+i][column+j]:
                        allSame=False
                        break
                if allSame==False: break
            if allSame:
                return Node(grid[row][column],True)
            n//=2
            topleft=dfs(n,row,column)
            topright=dfs(n,row,column+n)
            bottomleft=dfs(n,row+n,column)
            bottomright=dfs(n,row+n,column+n)
            return Node(0,False,topleft,topright,bottomleft,bottomright)
        return dfs(len(grid),0,0)
            