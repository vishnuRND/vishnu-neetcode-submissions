class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[left]:
                nums[left+1] = nums[i]
                left +=1
        return left+1
                
        