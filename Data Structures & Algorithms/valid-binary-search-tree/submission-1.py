# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, 1001, -1001)

    def traverse(self, root, maxi, mini):
        if not root:
            return True
        
        left, right = True, True
        if root.left:
            left = mini< root.left.val < root.val and self.traverse(root.left, root.val, mini)
        if root.right:
            right = maxi > root.right.val > root.val and self.traverse(root.right, maxi, root.val)
        return left and right