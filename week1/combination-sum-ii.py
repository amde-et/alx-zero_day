class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtracking(start, total, path):
            if total == target:
                ans.append(path)
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    return
                elif i > start and candidates[i] == candidates[i-1]:
                    continue
                else:
                    backtracking(i + 1, total + candidates[i], path + [candidates[i]])

        backtracking(0, 0, [])
        return ans