class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexOccurence = defaultdict(int)
        for index,num in enumerate(nums):
            if target-num in indexOccurence:
                return [indexOccurence[target-num],index]
            indexOccurence[num] = index