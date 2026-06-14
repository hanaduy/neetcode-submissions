# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # This is traverse for left, cur, right
        self.result = []
        self.traverse(root)
        return self.result[k-1]
    
    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)
        self.result.append(root.val)
        self.traverse(root.right)

        return

    