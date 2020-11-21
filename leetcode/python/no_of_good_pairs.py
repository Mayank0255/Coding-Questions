class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited[nums[i]] = True

            currentCount = nums.count(nums[i])
            if currentCount > 1:
                count += ((currentCount) * (currentCount - 1)) // 2
        return count
