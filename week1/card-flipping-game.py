class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        d = {}

        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                if fronts[i] not in d:
                    d[fronts[i]] = True
                if backs[i] not in d:
                    d[backs[i]] = True
            elif fronts[i] == backs[i]:
                d[fronts[i]] = False
        
        currmin =  float('inf')
        for key in d.keys():
            if d[key] == True:
                currmin = min(currmin, key)
        if currmin != float('inf'):
            return currmin
        return 0
                    
        
        

        