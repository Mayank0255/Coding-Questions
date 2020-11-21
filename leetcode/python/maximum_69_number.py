class Solution:
    def maximum69Number (self, num: int) -> int:
        numArray = [e for e in str(num)]

        for i, digit in enumerate(numArray):
            if int(digit) == 6:
                numArray[i] = '9'

                if int(''.join(numArray)) > num:
                    return int(''.join(numArray))
                else:
                    numArray[i] = '6'
        return int(''.join(numArray))
