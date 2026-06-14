# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = []
        maxi = -101
        self.traverse(root, maxi)
        return len(self.result)
    
    def traverse(self, root, maxi):
        if not root:
            return

        if root.val>=maxi:
            self.result.append(root.val)
            maxi = root.val
        self.traverse(root.left, maxi)
        self.traverse(root.right, maxi)
        return


