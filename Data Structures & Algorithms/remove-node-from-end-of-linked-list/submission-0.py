# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        fast = head
        for i in range(0,n):
            fast = fast.next
        
        slow = head
        prev=None
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev != None:
            prev.next = slow.next
            return head
        else:
            return head.next