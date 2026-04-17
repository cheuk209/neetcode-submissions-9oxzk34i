# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse l1 and l2
        l1_prev = None
        l2_prev = None
        while l1:
            temp = l1.next
            l1.next = l1_prev
            l1_prev = l1
            l1 = temp
        s = []
        while l1_prev:
            s.append(str(l1_prev.val))
            l1_prev = l1_prev.next
        
        s = int("".join(s))
        
        while l2:
            temp = l2.next
            l2.next = l2_prev
            l2_prev = l2
            l2 = temp
        k = []
        while l2_prev:
            k.append(str(l2_prev.val))
            l2_prev = l2_prev.next
        
        k = int("".join(k))

        result_str = str(s + k)
        dummy = ListNode()
        node = dummy
        for _ in range(len(result_str)-1, -1, -1):
            print(result_str[_])
            node.next = ListNode(int(result_str[_]))
            node = node.next
        return dummy.next
