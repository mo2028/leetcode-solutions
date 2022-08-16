# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        
        def dfs(root):
            nonlocal isBalanced
            if not root:
                return 0
                
            left = dfs(root.left)
            right = dfs(root.right)
            
            diff = abs(left - right)
            
            if diff > 1:
                isBalanced = False
#                 changed from "return" to "return #"
                return -1
            
            return 1+max(left, right)
        
        dfs(root)
        return isBalanced
            
            
        