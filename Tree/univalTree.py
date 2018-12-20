'''
DCP #8
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

'''
__author__ = 'Amitrajit Bose'
from collections import deque
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		self.children = [self.left,self.right]

def countUnival(root):
	if(not root):
		return
	else:
		if(not root.left and not root.right):
			#it is a left node
			return 1
		elif(not root.left):
			if(root.val == root.right.val):
				return 1+countUnival(root.right)
			else:
				return countUnival(root.right)
		elif(not root.right):
			if(root.val == root.left.val):
				return 1+countUnival(root.left)
			else:
				return countUnival(root.left)
		elif(root.left.val == root.val and root.right.val == root.val):
			return 1 + countUnival(root.left) + countUnival(root.right)
		else:
			return countUnival(root.left) + countUnival(root.right)

#helper function
def printTree(root):
    buf = deque()
    output = []
    if not root:
        print ('x')
    else:
        buf.append(root)
        count, nextCount = 1, 0
        while count:
            node = buf.popleft()
            if node:
                output.append(node.val)
                count -= 1
                for n in (node.left, node.right):
                    if n:
                        buf.append(n)
                        nextCount += 1
                    else:
                        buf.append(None)
            else:
                output.append('x')
            if not count:
                print (output)
                output = []
                count, nextCount = nextCount, 0
        # print the remaining all empty leaf node part
        output.extend(['x']*len(buf))
        print (output)

#Create the Tree
root=Node(0)
root.left=Node(1)
root.right=Node(0)
root.right.left=Node(1)
root.right.right=Node(0)
root.right.left.left=Node(1)
root.right.left.right=Node(1)
#root.right.right.left=Node(0)
#root.right.right.right=Node(0)

#printTree(root)
print(countUnival(root))