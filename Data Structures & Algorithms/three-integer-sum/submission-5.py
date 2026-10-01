class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def findTarget(target, i, j):
            result = list()
            while i < j:
                sum = nums[i] + nums[j] + target
                if sum == 0 :
                    result.append((nums[i], nums[j], target))
                    i+=1
                    j-=1
                    while nums[i] == nums[i-1] and i < j:
                        i+=1
                elif sum < 0:
                    i+=1
                else:
                    j-=1
            return result
        result = set()
        for index, num in enumerate(nums):
                Triplets = findTarget(num, index+1, len(nums)-1)
                for triplet in Triplets:
                        result.add(triplet)
        return list(result)