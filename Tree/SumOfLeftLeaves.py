# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.leftsum = 0
    
    def isLeaf(self, root):
        return not root.left and not root.right
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root:
            if root.left and self.isLeaf(root.left):
                self.leftsum += root.left.val
            self.sumOfLeftLeaves(root.left)
            self.sumOfLeftLeaves(root.right)
        return self.leftsum

