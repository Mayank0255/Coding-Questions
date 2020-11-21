from functools import reduce

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2*i)

        return reduce(lambda x, y: x ^ y, nums)
        
