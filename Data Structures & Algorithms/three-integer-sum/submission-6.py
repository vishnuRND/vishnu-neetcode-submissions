class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()
        n = len(nums) - 1

        for index, num in enumerate(nums):
                 i , j = index+1,n
                 if num > 0:
                    break

                 if index > 0 and num == nums[index-1]:
                    continue
                    
                 while i < j:
                    sum = nums[i] + nums[j] + num
                    if sum == 0 :
                        result.append((nums[i], nums[j], num))
                        i+=1
                        j-=1
                        while nums[i] == nums[i-1] and i < j:
                            i+=1
                    elif sum < 0:
                        i+=1
                    else:
                        j-=1

        return result