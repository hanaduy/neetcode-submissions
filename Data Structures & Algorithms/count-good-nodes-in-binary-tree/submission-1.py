# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []
        result = 0
        stack = deque([(root, -101)])

        while stack:
            cur, maxi = stack.pop()
            
            if cur.val >= maxi:
                maxi = cur.val
                result += 1
            if cur.right:
                stack.append((cur.right, maxi))
            if cur.left:
                stack.append((cur.left, maxi))

        return result


