class Solution:
    def sumZero(self, n: int) -> List[int]:
        currentN = n // 2
        res = []
        for i in range(-currentN, currentN + 1):
            res.append(i)
        if n % 2 == 0:
            res.remove(0)
        return res
