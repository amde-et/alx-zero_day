class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        arr = []
        
        def findSum(row, col):
            values = [(row - 1, col - 1),
            (row - 1, col), 
            (row - 1, col + 1), 
            (row, col), 
            (row + 1, col - 1), 
            (row + 1, col), 
            (row + 1, col + 1)]

            ans = 0

            for i in values:
                ans = ans + grid[i[0]][i[1]]
            
            return ans

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                arr.append(findSum(i, j))

        return max(arr)
        