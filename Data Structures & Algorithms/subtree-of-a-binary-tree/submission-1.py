# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def areSame(node1, node2):
            if node1 == None and node2 == None:
                return True
            if node1 and node2 and node1.val == node2.val:
                return areSame(node1.left, node2.left) and areSame(node1.right, node2.right)
            return False


        def dfs(node1):
            if subRoot == None:
                return True
            if node1 == None:
                return False
            if areSame(node1, subRoot):
                return True
            return dfs(node1.left) or dfs(node1.right)

        return dfs(root)
