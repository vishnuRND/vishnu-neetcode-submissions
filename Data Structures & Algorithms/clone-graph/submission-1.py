"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        newNodes = dict()
        def dfs(node):
            if node==None:
                return None
            if node.val in newNodes:
                return newNodes[node.val]
            nNode = Node(node.val)
            newNodes[node.val] = nNode
            for child in node.neighbors:
                nNode.neighbors.append(dfs(child))
            return nNode

        return dfs(node)
        