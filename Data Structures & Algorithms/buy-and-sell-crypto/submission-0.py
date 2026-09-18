class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = -sys.maxsize
        maxTillNow = -sys.maxsize
        N = len(prices)
        for i in range(N-1, -1, -1):
            maxProfit = max(maxProfit, maxTillNow-prices[i])
            maxTillNow = max(maxTillNow, prices[i])
        return maxProfit if maxProfit > 0 else 0