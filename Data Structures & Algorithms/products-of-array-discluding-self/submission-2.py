class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
                curr = nums[i]
                pre[i] = prev
                prev = prev*curr
        prev = 1
        for i in range(len(nums)-1, -1, -1):
                curr = nums[i]
                post[i] = prev
                prev = prev*curr
        for i in range(len(nums)):
            pre[i] *= post[i]

        return pre
        