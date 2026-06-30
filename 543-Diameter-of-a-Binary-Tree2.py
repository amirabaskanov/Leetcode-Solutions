# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # self. makes it a global variable for this class
        self.res = 0

        # another way to globalize is to make it a local variable "res = 0"
        # and then down before res max() you can type "nonlocal res"

        #return height
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res
