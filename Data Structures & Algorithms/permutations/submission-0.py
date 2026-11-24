class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = list()
        def recur(idx):
            if idx == len(nums):
                result.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[i],nums[idx] = nums[idx], nums[i]
                recur(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        recur(0)
        return result