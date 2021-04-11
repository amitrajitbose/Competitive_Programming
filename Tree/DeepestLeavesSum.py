# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        leafSum = [0]
        def dfs(node, level, maxDep, leafSum):
            if not node:
                return
            if level == maxDep:
                leafSum[0] += node.val
            else:
                dfs(node.left, level + 1, maxDep, leafSum)
                dfs(node.right, level + 1, maxDep, leafSum)
        dfs(root, 1, self.maxDepth(root), leafSum)
        return leafSum[0]
