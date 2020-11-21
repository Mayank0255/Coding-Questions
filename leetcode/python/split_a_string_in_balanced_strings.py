class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(accumulate(1 if c == "R" else -1 for c in s)).count(0)
