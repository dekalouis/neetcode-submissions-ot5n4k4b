# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init dummy node, with head as next, then declare left from dummy, right from the head
        # loop while n > 0, move right to the next, and reduce n by 1
        # loop separately while right exists, move both left and right forward
        # outside, set the next of left to be next next, return the new head which is the next 
        # node from dummy

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        return dummy.next