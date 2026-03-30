class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        check = []

        for num in nums:
            if num not in check:
                check.append(num)
            else:
                return True
        return False