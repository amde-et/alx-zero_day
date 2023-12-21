class Solution:
    def transpose(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        result = [[0] * rows for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        
        return result