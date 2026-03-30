class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        check = {}

        for num in nums:
            if num not in check:
                check[num] = 1
            else:
                return True
        return False