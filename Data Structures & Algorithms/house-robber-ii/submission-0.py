class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        def maxMoney(start, end):
            if start > end : 
                return 0
            dp = [0] * (end-start+1)
            for i in range(start, end):
                nonselect = dp[i-1] if i-1 >=0 else 0
                select = nums[i] + (dp[i-2] if i-2 >=0 else 0)
                dp[i] = max(nonselect,select)
            return dp[end-1]

        return max(maxMoney(0, n-1), maxMoney(1, n))