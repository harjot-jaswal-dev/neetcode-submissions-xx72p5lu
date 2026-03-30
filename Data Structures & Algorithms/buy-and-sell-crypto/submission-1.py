class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        l = 0
        r = 1

        while r < len(prices):
            total = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l += 1
            elif prices[l] <= prices[r]:
                r += 1
                max_profit = max(max_profit, total)
        return max_profit