/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) {
 *      val = x;
 *      left=null;
 *      right=null;
 *     }
 * }
 */
public class Solution {
    
    private int total = 0;
    private boolean ret = false;
    private TreeNode originRoot = null;
    
    public int solve(TreeNode root) {
        originRoot = root;
        total = getTotalSum(root);
        checkEqual(root);
        return ret ? 1:0;
    }
    
    private int getTotalSum(TreeNode root) {
        // post-order DFS
        if (root==null) return 0;
        return getTotalSum(root.left) + getTotalSum(root.right) + root.val;
    }
    
    public int checkEqual(TreeNode root) {
        // post-order DFS
        if (root==null || ret)  return 0; // skip checking
        int curSum = checkEqual(root.left) + checkEqual(root.right) + root.val;
        if (total-curSum==curSum) {
            if (root!=originRoot) { // skip the top level root
              ret = true;
              return 0;  
            }
            
        }
        return curSum;
    }
}

