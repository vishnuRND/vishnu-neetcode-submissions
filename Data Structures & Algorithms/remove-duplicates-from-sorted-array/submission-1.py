class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[left]:
                nums[left+1] = nums[i]
                left +=1
        return left+1
                
        