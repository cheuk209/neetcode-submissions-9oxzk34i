"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        return self.dfs(node, visited)

    def dfs(self, node, visited):
        if node is None:
            return None
        if node in visited:
            return visited[node]

        visited[node] = Node(node.val)

        for neighbor in node.neighbors:
            clone_neighbor = self.dfs(neighbor, visited)
            visited[node].neighbors.append(clone_neighbor)

        return visited[node]