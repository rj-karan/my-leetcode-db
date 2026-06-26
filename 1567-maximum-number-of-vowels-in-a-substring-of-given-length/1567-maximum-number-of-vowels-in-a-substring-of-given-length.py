class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        kk=set("aeiou")
        m=0
        ma=0
        for i in range(k):
            if s[i] in kk:
                m+=1
                ma=max(m,ma)
        for r in range(k,len(s)):
            l=r-k
            print(l)
            if s[l] in kk:
                m-=1
            if s[r] in kk:
                m+=1
            ma=max(m,ma)
        return ma

