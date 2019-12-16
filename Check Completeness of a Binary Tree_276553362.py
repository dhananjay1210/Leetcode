# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def tree_depth(root):
            if not root:
                return 0
            return 1 + tree_depth(root.left)
        self.depth = tree_depth(root)
        self.set = 1
        def dfs(root,level):
            if root.left==None and root.right==None:
                if level==self.depth:
                    return True
                elif level==self.depth-1 and self.set:
                    self.depth = level
                    self.set = 0
                    return True
                else:
                    return False
            elif root.left and root.right==None:
                if level==self.depth-1 and self.set:
                    self.depth = level
                    self.set = 0
                    return True
                else:
                    return False
            elif root.left==None and root.right:
                return False
            return dfs(root.left,level+1) and dfs(root.right,level+1)
        return dfs(root,1)
