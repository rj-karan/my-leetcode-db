class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        for i in range(len(s)):
            k=i
            t=i
            while (k>=0 and s[k]!=c):
                k-=1
            while (t<len(s) and s[t]!=c):
                t+=1
            if k==-1:
                a.append(t-i)
            elif t==len(s):
                a.append(i-k)
            else:
                a.append(min(i-k,t-i))
        return a
