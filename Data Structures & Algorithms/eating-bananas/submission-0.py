import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate = max(piles)
        sum_of_piles = sum(piles)
        valid_answers = []
        while min_rate <= max_rate:
            mid_rate = (min_rate + max_rate) // 2
            consumption_time = 0
            for banana_pile in piles:
                pile_consumption_time = math.ceil(banana_pile / mid_rate)
                consumption_time += pile_consumption_time
            if consumption_time <= h:
                valid_answers.append(mid_rate)
                max_rate = mid_rate - 1
            elif consumption_time > h:
                min_rate = mid_rate + 1
        return min(valid_answers)
