class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        # area = min(heights[l], heights[r]) * r - l
        max_area = -float("inf")
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
                l += 1
        return max_area