class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        alreadyFound = defaultdict(int)
        for index,num in enumerate(nums):
            if num in alreadyFound:
                matchFound =  abs(index - alreadyFound[num]) <=k 
                if matchFound:
                    return True
            alreadyFound[num] = index
        return False