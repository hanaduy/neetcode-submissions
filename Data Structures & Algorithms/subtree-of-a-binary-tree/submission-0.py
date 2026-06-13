# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        cur = self.traverse(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return cur or left or right
        

    def traverse(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        left = self.traverse(root.left, subRoot.left)
        right = self.traverse(root.right, subRoot.right)
        return left and right and root.val == subRoot.val