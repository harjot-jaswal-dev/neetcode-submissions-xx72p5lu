class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        curr_sum = sum(arr[:k])
        target_sum = k * threshold

        result = 0

        if curr_sum >= target_sum:
                result += 1

        for i in range(k, len(arr)):
            curr_sum += arr[i]
            curr_sum -= arr[i - k]

            if curr_sum >= target_sum:
                result += 1
        
        return result
