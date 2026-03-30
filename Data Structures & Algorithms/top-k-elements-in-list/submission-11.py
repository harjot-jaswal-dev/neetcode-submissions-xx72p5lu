class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        bucket = []
        result = []

        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        for key, value in counter.items():
            bucket[value].append(key)
        
        for i in bucket:
            if i:
                for n in i:
                    result.append(n)
        
        result = result[::-1]

        return result[:k]