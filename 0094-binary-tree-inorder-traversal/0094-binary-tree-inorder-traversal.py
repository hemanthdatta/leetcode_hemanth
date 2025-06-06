# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        
        def inorder_traversal(root):
            if root is None:
                return
            inorder_traversal(root.left)
            l.append(root.val)
            inorder_traversal(root.right)
            
        inorder_traversal(root)
        return l
            
                