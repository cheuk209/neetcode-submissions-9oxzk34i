import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            total_time_taken = 0
            for amount_bananas in piles:
                consumption_speed = math.ceil(amount_bananas/mid)
                total_time_taken += consumption_speed
            if total_time_taken > h:
                print("invalid")
                left = mid + 1
            elif total_time_taken <= h:
                right = mid
        return left
            