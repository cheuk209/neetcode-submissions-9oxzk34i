class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100
        max_price = 0
        max_profit = 0
        for index, value in enumerate(prices):
            min_price = min(min_price, value)
            profit = value - min_price
            max_profit = max(profit, max_profit)
        return max_profit