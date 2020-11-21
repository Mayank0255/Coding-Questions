class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summation = 0
        product = 1
        for i in str(n):
            summation += int(i)
            product *= int(i)
        return product - summation
