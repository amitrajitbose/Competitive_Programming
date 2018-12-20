# Definition for a binary tree node.
# Leetcode 297 - HARD
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(root==None):
            return ""
        def dfs(node):
            if node:
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
                #preorder traversal
            else:
                result.append('x')
        result = []
        dfs(root)
        return ' '.join(result)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(len(data)==0):
            return None
        def dfs():
            val=next(result)
            if(val == 'x'):
                return None
            else:
                node=TreeNode(int(val))
                node.left=dfs()
                node.right=dfs()
                return node
        result=iter(data.split())
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))