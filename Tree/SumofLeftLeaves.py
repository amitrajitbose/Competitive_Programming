# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        if root:
            if root.left and not root.left.left and not root.left.right:
                result += root.left.val # if left node is leaf
            else:
                result += self.sumOfLeftLeaves(root.left) # otherwise recurse down to left
            result += self.sumOfLeftLeaves(root.right) # then to right side, because we have to check full tree
        return result
