# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def rec(root1,root2):
            if root1==root2==None:
                return True
            if (not root1 and root2) or (root1 and not root2):
                return False
            if root1.val!=root2.val:
                return False
            return (rec(root1.left,root2.left) and rec(root1.right,root2.right)) or (rec(root1.left,root2.right) 
                and rec(root1.right,root2.left))
        ans = rec(root1,root2)
        if ans!=False:
            return True
        else:
            return False
