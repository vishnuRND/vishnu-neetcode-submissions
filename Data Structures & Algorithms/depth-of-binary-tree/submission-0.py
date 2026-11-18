# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recur(node):
            if node == None:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            return max(left, right)+1

        return recur(root)
        