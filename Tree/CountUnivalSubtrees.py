# https://leetcode.com/problems/count-univalue-subtrees
# LC 250 :: 250. Count Univalue Subtrees :: Premium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def isSubTreeUnival(self, root) -> bool:
        if not root:
            return True
        left = self.isSubTreeUnival(root.left)
        right = self.isSubTreeUnival(root.right)
        if not left or not right:
            return False
        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False
        self.count += 1
        return True
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.isSubTreeUnival(root)
        return self.count
