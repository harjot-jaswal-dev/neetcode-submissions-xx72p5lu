class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = []
        tracker_dict = {}
        result = []

        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num in nums:
            if num not in tracker_dict:
                tracker_dict[num] = 0
            tracker_dict[num] += 1
        
        for keys, values in tracker_dict.items():
            bucket[values].append(keys)
        
        for i in bucket:
            if i:
                for num in i:
                    result.append(num)
        
        result = result[::-1]
        
        return result[:k]

        
