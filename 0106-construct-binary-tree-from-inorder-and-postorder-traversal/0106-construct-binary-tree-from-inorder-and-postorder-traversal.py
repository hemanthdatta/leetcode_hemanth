# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def construct_binary_tree_post_and_inorder(inorder,postorder,inS,inE,poS,poE):
    #(inorder,postorder,0,len(inorder)-1,0,len(postorder)-1)
    if inS>inE or poS>poS:
        return None
    root_data=postorder[poE]
    root=TreeNode(root_data)
    linS=inS
    inR=-1
    for i in range(len(inorder)):
        if inorder[i]==root_data:
            inR=i
            break
       
    linE=inR-1
    lpoS=poS
    lpoE=lpoS-linS+linE
    rinS=inR+1
    rinE=inE
    rpoS=lpoE+1
    rpoE=poE-1
    
    root.left=construct_binary_tree_post_and_inorder(inorder,postorder,linS,linE,lpoS,lpoE)
    root.right=construct_binary_tree_post_and_inorder(inorder,postorder,rinS,rinE,rpoS,rpoE)
    
    return root
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return construct_binary_tree_post_and_inorder(inorder,postorder,0,len(inorder)-1,0,len(postorder)-1)
        