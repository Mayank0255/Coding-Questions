# Solution 1
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        x, y = [0] * n, [0] * m
        for i in indices:
            x[i[0]] += 1
            y[i[1]] += 1
        return sum([1 for j in y for i in x if (j+i) % 2])

# Solution 2
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for j in range(m)] for i in range(n)]
        
        for index in indices:
            for i in range(m):
                matrix[index[0]][i] += 1
            for j in range(n):
                matrix[j][index[1]] += 1

        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 == 1:
                    count += 1

        return count
