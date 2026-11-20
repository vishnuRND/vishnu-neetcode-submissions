class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result  = list()
        def recur(index, path):
            if index == len(nums):
                result.append(path)
                return
            recur(index+1, path)
            recur(index+1, path+[nums[index]])
        
        recur(0,[])
        return result

        