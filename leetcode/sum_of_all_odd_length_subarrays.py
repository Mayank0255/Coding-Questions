class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0

        for i in range(len(arr) + 1):
            for j in range(i + 1, len(arr) + 1):
                sub = arr[i:j]
                if len(sub) % 2 == 1:
                    res += sum(sub)
        return res
