class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lastUniqueIndex = -1
        for j in range(len(nums)):
            if nums[j] != val:
                nums[lastUniqueIndex+1] = nums[j]
                lastUniqueIndex += 1
        return lastUniqueIndex+1

