class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            targetNum = target - nums[i]
            if targetNum in res:
                return [res[targetNum], i]
            else:
                res[nums[i]] = i
        return []
