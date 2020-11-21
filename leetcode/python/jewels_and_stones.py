class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for l in J:
            count += S.count(l)
        return count
