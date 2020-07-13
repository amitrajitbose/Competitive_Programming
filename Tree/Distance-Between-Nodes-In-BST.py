"""
Given a binary search tree.
Return the distance between two nodes with given two keys B and C. It may be assumed that both keys exist in BST.

NOTE: Distance between two nodes is number of edges between them.

1 <= Number of nodes in binary tree <= 1000000
0 <= node values <= 10^9
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        lca = self.getLca(A, B, C)
        if lca:
            d1, d2 = [], [] # stores distance of B and C from LCA
            self.getLevel(lca, B, d1, 0)
            self.getLevel(lca, C, d2, 0)
            return d1[0] + d2[0]
        else:
            return -1
    def getLca(self, root, node1, node2):
        if not root:
            return root
        if root.val in [node1, node2]:
            return root
        left = self.getLca(root.left, node1, node2)
        right = self.getLca(root.right, node1, node2)
        if left and right:
            return root
        if left:
            return left
        return right
    def getLevel(self, root, data, d, level):
        if not root:
            return
        if root.val == data:
            d.append(level)
            return
        self.getLevel(root.left, data, d, level+1)
        self.getLevel(root.right, data, d, level+1)

