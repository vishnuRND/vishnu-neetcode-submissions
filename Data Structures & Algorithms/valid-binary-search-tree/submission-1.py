# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []

        def postOrder(node,min1, max1):
            if not node:
                return True
            return postOrder(node.left,min1, node.val) and postOrder(node.right,node.val, max1) and min1 < node.val < max1
        
        return postOrder(root, float('-inf'), float("inf"))