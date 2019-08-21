class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def lca(root: Node, n1: Node, n2: Node) -> Node:
    """
    Assumption:
    Both the child nodes n1 and n2 whose LCA we are
    looking for, they all actually exist in the same
    tree.
    """
    if not root:
        return None
    if root == n1 or root == n2:
        return root
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)
    if left and right:
        return root
    if not left and not right:
        return None
    if left:
        return left
    elif right:
        return right


# Testing Code
# For Tree Vizualization : https://youtu.be/13m9ZCB8gjw 
nine = Node(9)
five = Node(5)
eleven = Node(11, left=nine, right=five)
two = Node(2)
six = Node(6,left=two,right=eleven)
seven = Node(7)
thirteen = Node(13,left=seven)
eight = Node(8, right=thirteen)
three = Node(3, left=six, right=eight) # root

assert (lca(three, two, five).data == 6)
assert (lca(three, eight, eleven).data == 3)
assert (lca(three, eight, seven).data == 8)
