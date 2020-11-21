class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        lastIdx = len(nums) - 1
        return (nums[lastIdx] - 1) * (nums[lastIdx - 1] - 1)
