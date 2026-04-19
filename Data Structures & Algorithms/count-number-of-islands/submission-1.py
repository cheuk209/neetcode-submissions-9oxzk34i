class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # definitely a dfs problem
        visited = set()
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    self.dfs(r, c, visited, grid)
        return island_count

    def dfs(self, r, c, visited, grid):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited.add((r, c))

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            if new_r > len(grid)-1 or new_r < 0 or new_c > len(grid[0])-1 or new_c < 0:
                continue
            if (new_r, new_c) in visited:
                continue
            if grid[new_r][new_c] == "0":
                continue
            self.dfs(new_r, new_c, visited, grid)
        return 
        

        