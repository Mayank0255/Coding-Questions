class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        large = max(candies)
        for num in candies:
            if num + extraCandies >= large:
                res.append(True)
            else:
                res.append(False)
        return res
