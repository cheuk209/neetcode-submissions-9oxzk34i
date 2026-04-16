# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        new_head = ListNode(-1)
        new = new_head
        while current1 and current2:
            if current1.val == current2.val:
                new.next = current1
                new = new.next
                current1 = current1.next
                new.next = current2
                new = new.next
                current2 = current2.next
            elif current1.val < current2.val:
                new.next = current1
                new = new.next
                current1 = current1.next
            elif current2.val < current1.val:
                new.next = current2
                new = new.next
                current2 = current2.next
        if current1 and not current2:
            new.next = current1
        elif current2 and not current1:
            new.next = current2
        return new_head.next