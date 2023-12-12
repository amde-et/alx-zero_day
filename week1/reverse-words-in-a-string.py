class Solution:
    def reverseWords(self, s: str) -> str:
        lst1=s.split()[: : -1]
        str1= " ".join (lst1)
        result= str1.strip()
        return result 
        