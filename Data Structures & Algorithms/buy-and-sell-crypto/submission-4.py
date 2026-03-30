class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        l = 0
        r = l + 1

        while r < len(prices):
            total = prices[r] - prices[l]
            max_profit = max(max_profit, total)
            if prices[l] > prices[r]:
                l += 1
            elif prices[r] >= prices[l]:
                r += 1
        return max_profit