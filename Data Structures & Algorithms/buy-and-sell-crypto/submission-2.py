class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        profit_max = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy += 1
            elif prices[sell] >= prices[buy]:
                sell += 1
            profit_max = max(profit_max, profit)
        
        return profit_max
            

