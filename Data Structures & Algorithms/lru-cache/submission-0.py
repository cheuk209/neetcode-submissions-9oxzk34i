class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = LinkedNode(0,0)
        self.tail = LinkedNode(-1,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = LinkedNode(key, value)
            if len(self.cache) > self.capacity:
                temp = self.tail.prev
                self.remove(self.tail.prev)
                self.cache.pop(temp.key)
            self.insert(self.cache[key])

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        first_node = self.head.next
        self.head.next = node
        node.next = first_node
        node.prev = self.head
        first_node.prev = node


class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None