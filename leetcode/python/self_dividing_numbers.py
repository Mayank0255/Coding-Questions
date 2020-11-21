class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            if isSelfDividing(i):
                res.append(i)
        return res



def isSelfDividing(num):
    check = [int(i) for i in str(num)]

    for el in check:
        if el == 0 or num % el != 0:
            return False
    return True
