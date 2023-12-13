class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = {}

        for domain in cpdomains:
            domainArr = domain.split()  
            num = int(domainArr[0])
            if domainArr[1] in mp:
                mp[domainArr[1]] += num
            else:
                mp[domainArr[1]] = num
            for i in range(len(domainArr[1])):
                if domainArr[1][i] == ".":
                    subDomain = domainArr[1][i+1:]
                    if subDomain in mp:
                        mp[subDomain] += num
                    else:
                        mp[subDomain] = num
        result = []
        for key in mp:
            result.append(f"{mp[key]} {key}")
        return result
