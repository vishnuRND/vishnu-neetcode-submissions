class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxHeight = 0
        while left < right:
            maxHeight = max(maxHeight, (min(heights[left], heights[right]) * (right-left)))
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return maxHeight
        