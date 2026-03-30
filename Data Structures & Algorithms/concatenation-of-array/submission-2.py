class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        counter = 0
        while counter < 2:
            for num in nums:
                ans.append(num)
            counter += 1
        return ans
        