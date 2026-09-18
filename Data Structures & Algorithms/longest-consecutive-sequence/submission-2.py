class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        if not nums:
            return 0
        longest = -sys.maxsize
        for num in nums:
            if num-1 not in hash:
                count = 1
                x = num
                while x + 1 in hash:
                    count+=1
                    x+=1
                longest = max(longest,count)
        return longest
                
