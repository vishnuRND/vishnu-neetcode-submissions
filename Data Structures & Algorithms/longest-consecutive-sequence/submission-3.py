class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr_num = num
                count = 1
                while curr_num + 1 in nums_set:
                    count+=1
                    curr_num += 1
                res = max(res, count)
        return res

                
            
        