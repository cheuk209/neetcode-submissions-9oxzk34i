class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next == None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current_index = -1
        current_node = self.head

        while current_index + 1 < index and current_node:
            current_index += 1
            current_node = current_node.next
        
        # the next node will be deleted
        if current_node and current_node.next:
            # edge case
            if current_node.next == self.tail:
                self.tail = current_node
            current_node.next = current_node.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        current_node = self.head.next
        getVal = []
        while current_node:
            getVal.append(current_node.val)
            current_node = current_node.next
        return getVal
