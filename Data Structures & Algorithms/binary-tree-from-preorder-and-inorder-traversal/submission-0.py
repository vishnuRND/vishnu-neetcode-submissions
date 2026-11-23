# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preindex = 0
        inorderIndexes = dict()
        for idx, inorderele in enumerate(inorder):
            inorderIndexes[inorderele] = idx

        def dfs(inleft, inright):
            nonlocal preindex
            if inleft > inright or preindex == len(preorder):
                return None
            num = preorder[preindex]
            node = TreeNode(num)
            preindex+=1
            node.left = dfs(inleft, inorderIndexes[num]-1)
            node.right = dfs(inorderIndexes[num]+1,inright)
            return node
        
        return dfs(0, len(inorder))

        