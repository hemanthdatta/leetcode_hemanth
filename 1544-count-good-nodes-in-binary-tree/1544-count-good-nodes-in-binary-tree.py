class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Helper function to perform DFS traversal
        def solve(root, max_val):
            if not root:
                return 0

            # Check if the current node is a "good node"
            ans = 1 if root.val >= max_val else 0

            # Update the max_val as the max of current node's value and max_val
            new_max_val = max(max_val, root.val)

            # Recursively call solve for left and right subtrees
            ans += solve(root.left, new_max_val)
            ans += solve(root.right, new_max_val)

            return ans
        
        # Start DFS from the root with its own value as the initial max_val
        return solve(root, root.val)
