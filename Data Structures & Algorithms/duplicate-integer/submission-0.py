class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadySeen = defaultdict(int)
        for num in nums:
            if num in alreadySeen:
                return True
            else:
                alreadySeen[num] = True

        return False
         