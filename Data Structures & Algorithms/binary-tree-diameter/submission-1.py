# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def recur(node):
            if node == None:
                return 0,0
            left, ldiameter = recur(node.left)
            right, rdiameter = recur(node.right)
            return max(left, right)+1, max(ldiameter, rdiameter, left+right)

        h, d = recur(root)
        return d
        