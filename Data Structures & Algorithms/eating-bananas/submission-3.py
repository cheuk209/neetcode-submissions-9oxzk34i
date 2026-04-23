import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        # can only eat 1 pile per hour, no matter what
        optimal_range = (1, max_k)
        left = 1
        right = max_k
        min_speed = []
        while left <= right:
            print("what is min_speed", min_speed)
            mid = (left + right) // 2
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/mid)
            print("eating speed is", mid, hours_taken, "compared to", h)
            if hours_taken > h:
                left = mid + 1
            else:
                min_speed.append(mid)
                right = mid - 1
        return min(min_speed)
        
        
            