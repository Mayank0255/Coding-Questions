class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        sorted_list = sorted(nums)

        for i,n in enumerate(sorted_list):
            if n not in dic:
                dic[n] = i
        return [dic[n] for n in nums]
        
