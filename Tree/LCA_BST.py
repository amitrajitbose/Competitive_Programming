class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def getValue(self):
        return self.data

def lca(root: Node, n1: int, n2: int) -> Node:
    """
    This optimization applies only for a BST
    """
    while root:
        val = root.getValue()
        if val > n1 and val > n2:
            root = root.left
        elif val < n1 and val < n2:
            root = root.right
        else:
            return root # this is the LCA node
    return None # only if empty tree

"""
The root node is an ancestor to all nodes because there is a path from it to all other nodes. Therefore,
you can start at the root node and follow a path through the common ancestors of both nodes. When
your target values are both less than the current node, you go left. When they are both greater,
you go right. The first node you encounter that is between your target values is the lowest common
ancestor.
"""