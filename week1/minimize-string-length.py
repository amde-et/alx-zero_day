class Solution:
    def minimizedStringLength(self, s: str) -> int:
        res = []
        for i in s:
            res.append(i)
        news=set(res)
        return len(news)
#so basically here i use set becuase they remove duplicate automatically and that way i can remove all of them.
