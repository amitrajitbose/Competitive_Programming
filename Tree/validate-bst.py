# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)
    def isValid(self, node: TreeNode, maxbound: int, minbound: int) -> bool:
        # print(str(node), maxbound, minbound)
        if not node:
            return True
        if maxbound != None and node.val >= maxbound:
            return False
        if minbound != None and node.val <= minbound:
            return False
        return self.isValid(node.left, node.val, minbound) and self.isValid(node.right, maxbound, node.val)
