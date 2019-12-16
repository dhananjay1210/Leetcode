# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cam = 0
        if root==None:
            return 0
        
        def rec(root):
            if not root:
                return 2
            l = rec(root.left)
            r = rec(root.right)
            
            if l==2 and r==2:
                return 0
            if l==0 or r==0:
                self.cam = self.cam + 1
                return 1
            else:
                return 2
        atRoot = rec(root)
        return self.cam + (1 if atRoot==0 else 0)
