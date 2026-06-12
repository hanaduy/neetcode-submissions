"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_cur = dummy = Node(-1, None, None)
        cur = head

        idx = {}
        mapping = {}
        k = 0
        while cur:
            temp = Node(cur.val, cur.next, None)
            idx[k] = temp
            mapping[cur] = k 
            cur = cur.next
            new_cur.next = temp
            new_cur = new_cur.next
            k+=1
        # print(idx, mapping)

        cur = head
        new_cur = dummy.next
        while cur:
            if cur.random:
                # print(idx[mapping[cur.random]])
                new_cur.random = idx[mapping[cur.random]]
            else:
                new_cur.random = None
            cur = cur.next
            new_cur = new_cur.next

        return dummy.next