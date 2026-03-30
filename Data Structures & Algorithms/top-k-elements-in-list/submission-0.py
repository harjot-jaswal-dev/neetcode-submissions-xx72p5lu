class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counted_nums = {}
        buckets = []
        result = []
        n = len(nums)

        for num in nums:
            if num not in counted_nums:
                counted_nums[num] = 0
            counted_nums[num] += 1

        
        for i in range(n + 1):
            buckets.append([])
        
        for key, value in counted_nums.items():
            buckets[value].append(key)
        
        for i in buckets[::-1]:
            if i:
                for j in i:
                    result.append(j)
        
        return result[:k]
        

        

        

        