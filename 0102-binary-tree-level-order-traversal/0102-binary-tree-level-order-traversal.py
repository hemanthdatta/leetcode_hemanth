# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root])
        l=[]
        n=0

        while len(q)!=0:
            n=len(q)
            level=[]
            for i in range(n):
                curr_node=q.popleft()
                level.append(curr_node.val)

                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            l.append(level)
        return l

                
            
            


            



