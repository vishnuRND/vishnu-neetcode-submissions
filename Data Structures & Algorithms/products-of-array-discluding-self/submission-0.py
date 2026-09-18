class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_mul, right_mul = [0]*n,[0]*n
        prev = 1
        for i in range(n):
            left_mul[i] = prev
            prev = prev*nums[i]
        
        prev = 1
        for j in range(n-1, -1,-1):
            right_mul[j] = prev
            prev = prev*nums[j]

        result = list()
        for i in range(n):
            result.append(left_mul[i]*right_mul[i])

        return result