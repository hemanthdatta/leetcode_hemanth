# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def postorder_transversal(root):
            if root is None:
                return
            postorder_transversal(root.left)
            postorder_transversal(root.right)
            l.append(root.val)
        postorder_transversal(root)
        return l
        