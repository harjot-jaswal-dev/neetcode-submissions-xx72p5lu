class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        result = 0
        curr_arr = sum(arr[:k])
        
        if curr_arr / k >= threshold:
            result += 1

        for R in range(k, len(arr)):
            curr_arr -= arr[R - k]
            curr_arr += arr[R]
            if curr_arr / k >= threshold:
                result += 1
        
        return result