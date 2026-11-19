# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def postOrder(node,prevMax):
            if not node:
                return 0
            Lcount = postOrder(node.left, max(prevMax, node.val))
            Rcount = postOrder(node.right, max(prevMax, node.val))
            return Lcount+Rcount + (1 if node.val >= prevMax else 0)

        return postOrder(root, float("-inf"))