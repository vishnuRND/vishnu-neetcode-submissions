class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lasttillnow = prices[-1]
        profit = 0
        for i in range(len(prices)-2, -1, -1):
            if prices[i] < lasttillnow:
                profit = max(profit,  lasttillnow - prices[i])
            lasttillnow = max(lasttillnow, prices[i])
        return profit
