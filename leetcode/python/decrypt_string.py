class Solution:
    def freqAlphabets(self, s: str) -> str:
        right = len(s) - 1
        res = ''

        while right >= 0:
            if s[right] == '#':
                currentNum = s[right - 2: right]
                res += chr(int(currentNum) + 96)
                right -= 3
            else:
                res += chr(int(s[right]) + 96)
                right -= 1
        return res[::-1]
