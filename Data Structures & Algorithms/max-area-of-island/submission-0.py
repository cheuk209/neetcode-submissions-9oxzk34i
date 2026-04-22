class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                island_count = 0
                processed = self.dfs(grid, r, c)
                max_island_count = max(max_island_count, processed)
        return max_island_count

    def dfs(self, grid, r, c):
        print("what is wrong", r, c)
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] == 0:
            return 0
        island_count = 1
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        grid[r][c] = 0
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            processed = self.dfs(grid, new_r, new_c)
            island_count += processed
        return island_count