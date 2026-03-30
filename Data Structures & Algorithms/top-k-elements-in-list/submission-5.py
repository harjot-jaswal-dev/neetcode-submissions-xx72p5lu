class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_dict = {}

        bucket = []
        result = []

        n = len(nums)

        for i in range(n + 1):
            bucket.append([])


        for num in nums:

            if num not in counted_dict:
                counted_dict[num] = 0
            counted_dict[num] += 1
        
        for key, value in counted_dict.items():

            bucket[value].append(key)
        
        

        for i in bucket:
            if i:
                j = i
                for j in i:
                    result.append(j)
        result = result[::-1]

        answer = result[:k]

        return answer