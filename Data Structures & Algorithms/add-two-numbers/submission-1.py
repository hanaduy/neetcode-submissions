# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = new_start = ListNode(0, None)

        l1_start, l2_start = l1, l2
        carry = 0

        while l1_start or l2_start: 
            l1_val = 0 if not l1_start else l1_start.val
            l2_val = 0 if not l2_start else l2_start.val
                
            if l1_val + l2_val + carry >= 10:
                new_val = l1_val + l2_val + carry - 10
                new_node = ListNode(new_val, None)
                carry = 1
            else:
                new_val = l1_val + l2_val + carry
                new_node = ListNode(new_val, None)
                carry = 0
            new_start.next = new_node
            new_start = new_node
            if l1_start:
                l1_start = l1_start.next
            if l2_start:
                l2_start = l2_start.next
            if carry == 1:
                new_start.next = ListNode(1, None)
        return dummy.next

        

