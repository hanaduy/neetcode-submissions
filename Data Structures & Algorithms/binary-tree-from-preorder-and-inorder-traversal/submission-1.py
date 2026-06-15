# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = self.traverse(preorder, inorder)

        return head

    def traverse(self, preorder, inorder):
        if not preorder:
            return None

        cur_node = TreeNode(preorder[0], None, None)
        cur_idx = inorder.index(preorder[0])
        inorder_left = inorder[0:cur_idx]
        inorder_right = inorder[cur_idx+1:]
        
        cur_idx = preorder.index(preorder[0])
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        cur_node.left = self.traverse(preorder_left,inorder_left)
        cur_node.right = self.traverse(preorder_right,inorder_right)
        
        return cur_node

        
