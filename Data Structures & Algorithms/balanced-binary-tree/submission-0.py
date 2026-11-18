# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if node == None:
                return 0, True
            lheight, lbalanced = check_balance(node.left)
            rheight, rbalanced = check_balance(node.right)
            return max(lheight, rheight)+1, lbalanced and rbalanced and abs(lheight-rheight) <=1

        height, balanced = check_balance(root)
        return balanced