# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_list = self.traverse(root,p)
        q_list = self.traverse(root,q)
        result = None
        for i in range(min(len(p_list),len(q_list))):
            if p_list[i] == q_list[i]:
                result = p_list[i]
        return result
        
    
    def traverse(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if root.val == target.val:
                break
            elif root.val < target.val:
                root = root.right
            elif root.val > target.val:
                root = root.left
        return stack

        
