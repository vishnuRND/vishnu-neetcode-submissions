class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = 0
        for i in range(2, len(cost)+1):
            c = min(cost[i-1]+b,cost[i-2]+a)
            a, b = b, c
        return b
        