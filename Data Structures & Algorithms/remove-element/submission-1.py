class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0
        unique = set(nums)
        if len(unique) == 1:
            return 0
        while i < j:
            if nums[i] == val:
                while j > 0 and nums[j] == val:
                    j-=1
                if i < j: 
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                    i += 1
            else:
                i += 1
        while j > 0 and nums[j] == val:
                    j-=1
        return j+1

        
        