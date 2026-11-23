class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [1] * n
        for i in range(m-2, -1, -1):
            curr_dp = [0 for _ in range(n)]
            for j in range(n-1, -1, -1):
                curr_dp[j] = dp[j] + (curr_dp[j+1] if j+1 < n else 0)
            dp = curr_dp
        return dp[0]
        