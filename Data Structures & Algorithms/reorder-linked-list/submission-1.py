# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        # we need to reach midpoint for right first
        length = 0
        while left:
            left = left.next
            length += 1
        mid = length // 2
        right = head
        for _ in range(mid):
            right = right.next
        # left = [0, 1, 2]
        # right = [3, 4, 5, 6]

        prev = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        right = prev
        # left = [0, 1, 2]
        # right = [6, 5, 4, 3]

        dummy = head
        left = head
        while left and right.next:
            temp_l = left.next
            temp_right = right.next
            left.next = right
            right.next = temp_l
            left = temp_l
            right = temp_right

