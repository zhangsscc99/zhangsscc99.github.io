class Solution {
    LinkedList<Integer> res = new LinkedList<>();
    public List<Integer> preorderTraversal(TreeNode root) {
        
        traverse(root);
        return res;

    }

    private void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        res.addLast(root.val);
        traverse(root.left);
        traverse(root.right);
        
    }
}