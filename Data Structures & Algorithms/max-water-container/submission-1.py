class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_vol = 0

        l = 0
        r = len(heights) - 1

        while l < r:

            volume = min(heights[l], heights[r]) * (r - l)

            if volume > max_vol:
                max_vol = volume
            if heights[l] < heights[r]:
                l +=1
                continue
            if heights[r] < heights[l]:
                r -=1
                continue
            else:
                l += 1
                r -=1
        return max_vol
        