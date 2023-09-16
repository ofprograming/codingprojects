

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        if root is None: 
            return 0 
        return 1 + max(map(self.maxDepth, root.children or [None]))