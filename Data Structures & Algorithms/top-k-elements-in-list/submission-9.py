class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        tracker = {}
        bucket = []
        result = []

        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num in nums:
            if num not in tracker:
                tracker[num] = 0
            tracker[num] += 1
        
        for key, value in tracker.items():
            bucket[value].append(key)
        
        for i in bucket:
            if i:
                for num in i:
                    result.append(num)
        result = result[::-1]
        return result[:k]
        

        
        

        
