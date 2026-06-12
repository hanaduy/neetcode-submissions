# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Slow and fast pointer, point to the middle
        slow = fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        # Middle reverse, get the last item from the second half
        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        
        # Merge two lists
        second = prev
        first = head
        while second.next:
            list1 = first.next
            list2 = second.next
            first.next = second
            second.next = list1
            first = list1
            second = list2
        


