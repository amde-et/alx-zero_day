class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans = [0]
        cand = most = nums.count(1)
        for i, x in enumerate(nums): 
            if x == 0: 
                cand += 1
            elif x == 1: 
                cand -= 1
            if cand > most: 
                ans, most = [i+1], cand
            elif cand == most: 
                ans.append(i+1)
        return ans 