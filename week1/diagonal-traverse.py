from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])
        diagonalDict = defaultdict(list)
	
        for r in range(R):
            for c in range(C):
                diagonalDict[r+c].append(mat[r][c])
        ans = []
        for i, value in enumerate(diagonalDict.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        return ans