class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_num = sorted(nums)
        result = []

        for i in range(len(sorted_num)):
            l = i + 1
            r = len(sorted_num) - 1

            if i > 0:
                if sorted_num[i] == sorted_num[i - 1]:
                    i += 1
                    continue

            while l < r:
                total = sorted_num[i] + sorted_num[l] + sorted_num[r]
                if total > 0:
                    r -= 1
                    continue
                elif total < 0:
                    l += 1
                    continue
                elif total == 0:
                    pair = [sorted_num[i],sorted_num[l],sorted_num[r]]
                    result.append(pair)
                
                while l < r and sorted_num[l] == sorted_num[l + 1]:
                    l += 1
                
                while r > l and sorted_num[r] == sorted_num[r - 1]:
                    r -= 1
                l += 1
                r -= 1
        return result