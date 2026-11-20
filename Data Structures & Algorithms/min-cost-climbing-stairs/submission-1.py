class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a = 0
        b = 0
        for i in range(2, n+1):
            c = min(cost[i-1]+b,cost[i-2]+a)
            a, b = b, c
        return b
        