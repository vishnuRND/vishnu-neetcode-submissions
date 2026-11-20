class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        def recur(index, path, curr_sum):
            if curr_sum > target:
                return 
            if curr_sum == target:
                result.append(path)
                return 
            if index == len(nums):
                return 
            recur(index, path+[nums[index]], curr_sum + nums[index])
            recur(index+1, path, curr_sum)

        recur(0, [],0)
        return result
        