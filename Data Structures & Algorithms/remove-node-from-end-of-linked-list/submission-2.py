# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        for _ in range(n+1):
            if right == None:
                return head.next
            right = right.next
        # inserted pointer, now need to travel to til the end along with left

        while right:
            left = left.next
            right = right.next
        ## now left is finally at the point 

        if left and left.next:
            left.next = left.next.next

        return head