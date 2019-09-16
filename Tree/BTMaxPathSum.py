#LCH124

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = -float('inf')
        
        def maxPathSumUtil(root: TreeNode) -> int:
            if not root:
                return 0 # base case
            leftsum = maxPathSumUtil(root.left)
            rightsum = maxPathSumUtil(root.right)
            self.maxsum = max(self.maxsum, root.val, root.val + leftsum, root.val + rightsum, root.val + leftsum + rightsum)
            return max(0, leftsum, rightsum) + root.val
        
        maxPathSumUtil(root)
        return self.maxsum