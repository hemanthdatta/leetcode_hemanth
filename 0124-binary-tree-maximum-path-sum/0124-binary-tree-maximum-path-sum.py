# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float(-inf)
        def maxPathSum1(root):
            if root is None:
                return 0
            leftsum=max(0,maxPathSum1(root.left))
            rightsum=max(0,maxPathSum1(root.right))
            self.maxi=max(self.maxi,leftsum+rightsum+root.val)
            return root.val+max(leftsum,rightsum)
        maxPathSum1(root)
        return self.maxi

        


        