# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = 0

    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if node:
            if node.left:
                left = self.maxDepth(node.left)
            else:
                left = 0
            if node.right:
                right = self.maxDepth(node.right)
            else:
                right = 0
            depth = 1 + max(left, right)  

            return depth
        else:
            return 0

        
        

