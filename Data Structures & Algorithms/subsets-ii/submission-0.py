class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()
        def recur(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            recur(index+1, path+[nums[index]])
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index+=1
            recur(index+1, path)

        recur(0, [])
        return result 
        