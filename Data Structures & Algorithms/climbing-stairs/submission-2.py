class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {}
        return self.dp(n, visited)


    def dp(self, n, visited):
        if n == 1 or n == 2:
            return n
        if n in visited:
            return visited[n]

        res = self.dp(n-1, visited) + self.dp(n-2, visited)
        visited[n] = res

        return res