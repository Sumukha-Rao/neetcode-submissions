"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        track={}
        if not node:
            return
        def dfs(gnode):
            if gnode in track:
                return track[gnode]
            clone=Node(gnode.val,[])
            track[gnode]=clone
            for i in gnode.neighbors:
                clone.neighbors.append(dfs(i))
            return clone
        return dfs(node)
      