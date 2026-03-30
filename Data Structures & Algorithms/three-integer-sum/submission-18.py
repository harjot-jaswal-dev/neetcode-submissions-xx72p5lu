class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)
        result = []

        if len(nums) < 3:
            return []

        for i in range(len(sorted_nums)):
            set_pointer = i
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                total = sorted_nums[set_pointer] + sorted_nums[l] + sorted_nums[r]
                if total == 0:
                    to_add = [sorted_nums[set_pointer], sorted_nums[l] , sorted_nums[r]]
                    if to_add not in result:
                        result.append(to_add)
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                    continue
                else:
                    l +=1
                    continue
        
        return result
