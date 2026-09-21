class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
        count = defaultdict(int)
        N = len(nums)
        for num in nums:
            count[num] += 1
            if count[num] > N  // 2:
                return num
        return 0