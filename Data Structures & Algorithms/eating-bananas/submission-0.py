class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 0
        def countNumOfDays(rate):
            days = 0
            for pile in piles:
                days += ((pile+rate-1)//rate)
            return days
        while left <= right:
            mid = (left + right) // 2
            if countNumOfDays(mid) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid+1
        return res
        