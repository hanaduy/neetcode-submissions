# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result, height = self.traverse(root)
        return result


    def traverse(self, root):
        if not root:
            return True, 0
        
        good_left, left_height = self.traverse(root.left)
        good_right, right_height = self.traverse(root.right)

        if abs(left_height - right_height) <= 1 and good_left and good_right:
            return True, max(left_height, right_height)+1
        else:
            return False, max(left_height, right_height)+1