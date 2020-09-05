# Solution 1
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' + 'b' * (n - 1)
        else:
            return 'a' * n

# Solution 2    
class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * n if n%2 == 1 else 'a' + 'b' * (n - 1)
