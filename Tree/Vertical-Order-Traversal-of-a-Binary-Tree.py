# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        hmap = defaultdict(list)
        queue = deque([(root, 0, 0)])
        while queue:
            node, col, dep = queue.popleft()
            if node:
                hmap[col].append((node.val, dep))
                queue.append((node.left, col-1, dep+1))
                queue.append((node.right, col+1, dep+1))
        res = []
        for k,v in sorted(hmap.items()):
            # sort by level and then by value
            # values which have lower depth should come first
            # values in same depth, should be ordered in ascending order of keys
            # first priority = depth = x[1], then value = x[0] --> (x[1], x[0])
            res.append([a for a,b in sorted(v, key=lambda x:(x[1], x[0]))])
        return res
