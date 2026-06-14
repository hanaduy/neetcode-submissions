# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = defaultdict(list)
        levels = []
        self.traverse(root, 0)
        level = 0
        while level in self.result:
            levels.append(self.result[level])
            level += 1
            
        return levels
    
    def traverse(self, root, level):
        if not root:
            return
        
        if level not in self.result:
            self.result[level] = [root.val]
        else:
            self.result[level].append(root.val)

        self.traverse(root.left, level+1)
        self.traverse(root.right, level+1)

        return

        
