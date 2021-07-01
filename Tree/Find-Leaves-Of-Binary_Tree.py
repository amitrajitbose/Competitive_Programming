# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        while not self.isLeaf(root):
            res.append(self.getNextLeaves(root))
        res.append([root.val])
        return res
            
    def isLeaf(self, root) -> bool:
        return root and not root.left and not root.right
    
    def getNextLeaves(self, root) -> List[int]:
        if not root:
            return []
        q = [(root, -1)]
        leaf = []
        while q:
            node, parent = q.pop(0)
            if not self.isLeaf(node):
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            else:
                leaf.append(node.val)
                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None
        return leaf
