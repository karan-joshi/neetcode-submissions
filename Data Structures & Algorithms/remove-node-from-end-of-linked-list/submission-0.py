# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first_pointer = head
        second_pointer = head
        i = 0
        while second_pointer and i < n:
            second_pointer = second_pointer.next
            i += 1

        prev = None
        while second_pointer:
            second_pointer = second_pointer.next
            prev = first_pointer
            first_pointer = first_pointer.next

        if first_pointer == head:
            return head.next
        
        prev.next = first_pointer.next
        first_pointer.next = None

        return head

        

        