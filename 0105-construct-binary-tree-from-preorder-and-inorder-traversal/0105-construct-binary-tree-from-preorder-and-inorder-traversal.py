# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def construct_binary_tree(inorder,preorder,inS,inE,prS,prE):
    if inS>inE or prS>prS:
        return None
    # inS=inorder[0]
    # inE=inorder[len(inorder)-1]
    # prS=preorder[0]
    # prE=preorder[len(preorder)-1]
    root_data=preorder[prS]
    root=TreeNode(root_data)
    linS=inS
    inR=-1
    for i in range(len(inorder)):
        if inorder[i]==root_data:
            inR=i
            break
       
    linE=inR-1
    lprS=prS+1
    lprE=linE-linS+lprS
    rinS=inR+1
    rinE=inE
    rprS=lprE+1
    rprE=prE
    
    root.left=construct_binary_tree(inorder,preorder,linS,linE,lprS,lprE)
    root.right=construct_binary_tree(inorder,preorder,rinS,rinE,rprS,rprE)
    
    return root
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return construct_binary_tree(inorder,preorder,0,len(inorder)-1,0,len(preorder)-1)
        