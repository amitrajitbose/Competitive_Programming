# https://leetcode.com/problems/range-sum-query-mutable/
from math import ceil, log2

class SegmentTree:
    def __init__(self, nums):
        self.arr = nums
        self.low, self.high = 0, len(self.arr)-1
        self.buildSegmentTree(nums)
    
    def _build_tree(self, nums, tree, idx, low, high):
        if low == high:
            tree[idx] = nums[low]
        else:
            mid = (high + low) // 2
            self._build_tree(nums, tree, (idx*2)+1, low, mid) # recurse left child
            self._build_tree(nums, tree, (idx*2)+2, mid+1, high) # recurse right child
            tree[idx] = tree[(idx*2)+1] + tree[(idx*2)+2] # merge
    
    def buildSegmentTree(self, nums):
        if not nums:
            return
        treeHeight = ceil(log2(len(nums)))
        tree = [0] * (2 ** (treeHeight + 1))
        self._build_tree(nums, tree, 0, self.low, self.high)
        self.tree = tree
    
    def rangeQuery(self, l, h):
        return self._rangeQuery(l, h, 0, self.low, self.high)
    
    def _rangeQuery(self, l, h, idx, low, high) -> int:
        if l > high or h < low:
            return 0 # no overlap
        if l <= low and high <= h:
            return self.tree[idx] # complete overlap
        # partial overlap
        mid = (low + high) // 2
        return self._rangeQuery(l,h,(idx*2)+1,low,mid) + self._rangeQuery(l,h,(idx*2)+2,mid+1,high)
    
    def update(self, i, val):
        diff = val - self.arr[i] # delta change
        self.arr[i] = val
        self._update_helper(i, diff, 0, self.low, self.high)
    
    def _update_helper(self, i, val, idx, low, high):
        if i > high or i < low:
            return
        self.tree[idx] += val
        if low != high:
            # propagate the update
            mid = (low + high) // 2
            self._update_helper(i, val, (idx*2)+1, low, mid)
            self._update_helper(i, val, (idx*2)+2, mid+1, high)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = SegmentTree(nums)
        self.segTree.buildSegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segTree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.rangeQuery(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


