class Solution {
    int res = 0;
    int depth = 0;
    public int maxDepth(TreeNode root) {
        traverse(root);
        return res;


        

    }

    private void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        depth++;
        if (root.left == null && root.right == null) {
            res = Math.max(res, depth);
        }
        traverse(root.left);
        traverse(root.right);
        depth--;
        
    }

}