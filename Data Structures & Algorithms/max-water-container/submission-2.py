class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        l = 0

        r = len(heights) - 1

        while l < r:
            
            max_water = min(heights[l], heights[r]) * (r - l)
            
            if max_water > result:
                result = max_water
            
            if heights[l] < heights[r]:
                l += 1
                continue
            elif heights[r] < heights[l]:
                r -= 1
                continue
            elif heights[l] == heights[r]:
                l += 1
                r -= 1
                
            
        return result