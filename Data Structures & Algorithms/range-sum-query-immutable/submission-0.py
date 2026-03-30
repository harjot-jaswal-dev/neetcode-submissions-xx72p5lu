class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0

        for n in nums:
            total += n
            self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        right_prefix = self.prefix[right]
        left_prefix = self.prefix[left]
        if left > 0:
            left_prefix = self.prefix[left - 1]
        else:
            left_prefix = 0
        return right_prefix - left_prefix
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)