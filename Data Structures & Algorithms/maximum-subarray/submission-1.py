class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        result = float("-inf")
        for num in nums:
            curr_sum += num
            if curr_sum <= num:
                curr_sum = num
            result = max(result, curr_sum)
        return result
        