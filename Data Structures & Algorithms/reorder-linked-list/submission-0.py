# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        right = head
        while right and right.next:
            right = right.next.next
            left = left.next
        
        right = left.next
        left.next = None

        prev = None
        # reversing linked list
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        
        right = prev
        left = head

        # merging
        while left and right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next


