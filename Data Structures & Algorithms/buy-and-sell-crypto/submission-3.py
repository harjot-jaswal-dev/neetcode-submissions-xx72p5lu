class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 0
        profit = 0

        while sell < len(prices):
            total = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy += 1
            elif prices[sell] >= prices[buy]:
                sell += 1
            profit = max(profit, total)
        return profit