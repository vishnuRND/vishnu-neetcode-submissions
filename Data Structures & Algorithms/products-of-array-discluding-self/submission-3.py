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
                curr = nums[i]
                post[i] = prev
                prev = prev*curr
        for i in range(N):
            pre[i] *= post[i]

        return pre
        