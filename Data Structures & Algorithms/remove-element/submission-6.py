class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lastUniqueIndex = -1
        for j in range(len(nums)):
            if nums[j] != val:
                lastUniqueIndex += 1
                nums[lastUniqueIndex] = nums[j]  
        return lastUniqueIndex+1

