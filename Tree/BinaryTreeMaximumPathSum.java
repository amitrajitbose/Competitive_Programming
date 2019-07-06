/*
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes 
from some starting node to any node in the tree along the 
parent-child connections. The path must contain at least one node 
and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int max = Integer.MIN_VALUE;
    
    /* Custom Method To Find Max Of N Numbers*/
    public static Integer mmax(Integer... vals)
    {
        Integer ret = Integer.MIN_VALUE;
        for (Integer val : vals) {
            if (val > ret) {
                ret = val;
            }
        }
        return ret;
    }
    
    public int traverse(TreeNode node){
        if (node == null)
            return 0;
        int max_left = traverse(node.left);
        int max_right = traverse(node.right);
        this.max = mmax(this.max, node.val, node.val + max_left + max_right, max_left + node.val, max_right + node.val);
        System.out.println(this.max);
        return mmax(max_left, max_right, 0) + node.val;
        
    }
    public int maxPathSum(TreeNode root) {
        traverse(root);
        return max;
    }
}