"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        random_hashmap = {}
        if not head:
            return None
        while curr:
            new_node = Node(curr.val, curr.next)
            random_hashmap[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            random_node = curr.random
            if random_node:
                random_hashmap[curr].random = random_hashmap[random_node]
            if curr.next:
                random_hashmap[curr].next = random_hashmap[curr.next]
            curr = curr.next
        curr = head
        return random_hashmap[curr]
