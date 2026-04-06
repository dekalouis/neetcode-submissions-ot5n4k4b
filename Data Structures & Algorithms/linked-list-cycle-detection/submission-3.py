# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        hash = set()

        while current is not None:
            if current in hash:
                return True
            hash.add(current)
            current = current.next
        return False
        
        