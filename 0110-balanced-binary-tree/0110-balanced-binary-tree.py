# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalanced1(root):
            if root is None:
                return 0,True
    
            lh,lb=isBalanced1(root.left)
            rh,rb=isBalanced1(root.right)
            currh=1+max(rh,lh)
    
            currb=lb and rb and abs(lh - rh)<=1
    
            return currh,currb
        h,b=isBalanced1(root)
        return b
        