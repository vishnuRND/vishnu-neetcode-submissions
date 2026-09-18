class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxTillNow = -sys.maxsize
        N = len(prices)
        for i in range(N-1, -1, -1):
            maxProfit = max(maxProfit, maxTillNow-prices[i])
            maxTillNow = max(maxTillNow, prices[i])
        return maxProfit