class Solution {
    int res = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        maxDepth(root);
        return res;


    }
    

    private int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftMax = maxDepth(root.left);
        int rightMax = maxDepth(root.right);

        int maxDiameter = leftMax + rightMax;
        res = Math.max(maxDiameter, res);

        return 1 + Math.max(leftMax, rightMax);
    }
}