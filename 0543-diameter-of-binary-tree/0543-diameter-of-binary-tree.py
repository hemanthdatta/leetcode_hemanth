# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root):
            if root is None:
                return 0,0
            
            lh,ld=diameter(root.left)
            rh,rd=diameter(root.right)

            d=max(ld,rd,lh+rh)
            h=1+max(lh,rh)
            return h,d
        h,d=diameter(root)
        return d
        