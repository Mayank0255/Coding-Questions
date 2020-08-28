class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for idx, i in enumerate(index):
            target.insert(i, nums[idx])
        return target
