class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        count = 0

        top = 0
        while top < height:
            left = 0
            while left < width:
                if grid[top][left] < 0:
                    breadth = width - left
                    length = height - top

                    width -= breadth
                    count += breadth * length
                left += 1
            top += 1
        return count
