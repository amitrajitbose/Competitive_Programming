'''
DCP #3
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def serialize(root):
    """Encodes a tree to a single string.
    :type root: Node
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
            result.append('-1')
    result = []
    dfs(root)
    #print(result)
    return ' '.join(result)
        

def deserialize(data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: Node
    """
    if(len(data)==0):
        return None
    def dfs():
        val=next(result)
        if(val == '-1'):
            return None
        else:
            node=Node(val) #reconstructing tree
            node.left=dfs()
            node.right=dfs()
            return node
    result=iter(data.split())
    return dfs()

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'