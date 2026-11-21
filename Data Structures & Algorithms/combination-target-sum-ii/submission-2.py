class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        visited = set()
        candidates.sort()
        def recur(index, curr_sum, path):
            if curr_sum == target:
                 result.append(path)
                 return 
            if index == len(candidates) or curr_sum > target:
                return 
            recur(index+1, curr_sum+candidates[index], path+[candidates[index]])
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            recur(index+1, curr_sum, path)

        recur(0,0 ,[])
        return result