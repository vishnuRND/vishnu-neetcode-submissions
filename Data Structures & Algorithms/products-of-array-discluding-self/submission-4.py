class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pre = [1] * N
        post = [1] * N
        prev = 1
        for i in range(N):
                curr = nums[i]
                pre[i] = prev
                prev = prev*curr
        prev = 1
        for i in range(N-1, -1, -1):
                pre[i] *= prev
                prev *= nums[i]

        return pre
        