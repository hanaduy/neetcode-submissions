# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.mapping = {}
        self.preorder = preorder
        self.inorder = inorder
        self.cur_idx = 0
        for k, v in enumerate(inorder):
            self.mapping[v] = k
        print(self.mapping)
        head = self.traverse(0, len(preorder)-1)
        return head

    def traverse(self, in_left, in_right):
        if in_left > in_right:
            return None

        cur = preorder[self.cur_idx]
        self.cur_idx += 1
        root = TreeNode(cur, None, None)

        mid_idx = self.mapping[cur]
        root.left = self.traverse(in_left,mid_idx-1)
        root.right = self.traverse(mid_idx+1, in_right)
        return root


        
        
