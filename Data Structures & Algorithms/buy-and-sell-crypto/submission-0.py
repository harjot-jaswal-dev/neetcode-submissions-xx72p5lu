class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices):
            total = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l += 1
                #r += 1
            elif prices[l] <= prices[r]:
                max_profit = max(max_profit, total)
                r += 1
            
        return max_profit