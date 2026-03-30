class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        maps = {}
        bucket = []
        result = []
        counter = 0

        for num in nums:

            if num not in maps:
                maps[num] = 0
            maps[num] += 1
        
        for i in range(len(nums) + 1):
            bucket.append([])
        
        for key, value in maps.items():

            bucket[value].append(key)
        
        for i in range(len(bucket) -1, -1, -1):

            if bucket[i]:
                for num in bucket[i]:
                    if counter < k:
                        counter += 1
                        result.append(num)
        return result

    



        
        