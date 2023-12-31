class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def inorderTraversal(self, tree):
        if tree != None: 
            return self.inorderTraversal(tree.left) + [tree.val] + self.inorderTraversal(tree.right) 
        else:  
            return [] 