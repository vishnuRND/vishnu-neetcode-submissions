class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        prev = 1
        for i in range(n):
            result[i] = prev
            prev = prev*nums[i]
        
        prev = 1
        for j in range(n-1, -1,-1):
            result[j] *= prev
            prev = prev*nums[j]

        return result