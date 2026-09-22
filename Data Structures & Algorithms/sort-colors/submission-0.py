class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Count = Counter(nums)
        index = 0 
        zero_last_index = index + Count[0]
        one_last_index = zero_last_index + Count[1]
        two_last_index = one_last_index + Count[2]
        while index < zero_last_index:
            nums[index] = 0
            index += 1
        while index < one_last_index:
            nums[index] = 1
            index += 1
        while index < two_last_index:
            nums[index] = 2
            index += 1
    
        