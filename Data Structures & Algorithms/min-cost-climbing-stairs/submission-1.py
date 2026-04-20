class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top-down approach
        cache = {}
        first = self.climbing_cost(0, cost, cache)
        second = self.climbing_cost(1,cost, cache)
        return min(first, second)

    def climbing_cost(self, floor, cost, cache) -> int:
        if floor == len(cost): # if we are already at target
            return 0

        if floor > len(cost):
            return float('inf')

        if floor in cache:
            return cache[floor]
        
        min_cost = cost[floor] + min(self.climbing_cost(floor+1, cost, cache), self.climbing_cost(floor+2, cost, cache))
        cache[floor] = min_cost
        return min_cost