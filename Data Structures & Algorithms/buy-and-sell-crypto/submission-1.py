class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
        return max_profit