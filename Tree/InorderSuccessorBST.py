# https://leetcode.com/problems/inorder-successor-in-bst/
# LintCode 448

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        possibleSuccessor = None
        curr = root
        while curr:
            if curr.val > p.val:
                possibleSuccessor = curr
                curr = curr.left # try to look for a lesser value, nearer successor
            else:
                curr = curr.right # get to the search node so that we can find successor
        return possibleSuccessor

