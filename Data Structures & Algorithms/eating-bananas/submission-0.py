class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        min_time = max(piles)

        def hours_helper(piles, speed):
            total_hours = 0
            for pile in piles:
                hours_in_pile = (pile + speed - 1) // speed
                total_hours += hours_in_pile
            return total_hours
        
        while left <= right:
            mid = (left + right) // 2
            if hours_helper(piles, mid) <= h:
                min_time = mid
                right = mid - 1
            elif hours_helper(piles, mid) > h:
                left = mid + 1
            
        return min_time


        