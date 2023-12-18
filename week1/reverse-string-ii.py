class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        def helper(org=s):
            nonlocal ans
            n = 2*k
            if len(org)<k:
                ans += org[::-1]
                return
            else:
                while len(org) > k:
                    t = org[0:n]
                    org = org[n:]
                    x = t[0:k]
                    t = t[k:]
                    ans += x[::-1] + t
                if len(org) <=k:
                    ans += org[::-1]
            return
        helper()
        return ans