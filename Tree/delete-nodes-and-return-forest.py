# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Author: @amitrajitbose

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        resultset = set([root])
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                queue.extend([node.left, node.right]) # copy of references
                if node.val in to_delete:
                    if node in resultset: resultset.remove(node)
                    if node.left: resultset.add(node.left)
                    if node.right: resultset.add(node.right)
                else:
                    if node.left and node.left.val in to_delete: node.left = None
                    if node.right and node.right.val in to_delete: node.right = None
        return list(resultset)
