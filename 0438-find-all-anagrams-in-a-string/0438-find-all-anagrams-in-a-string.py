class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        a=[]        
        sc=defaultdict(int)
        pc=defaultdict(int)
        for i in range(len(p)):
            sc[s[i]]+=1
            pc[p[i]]+=1
        if sc==pc:
            a.append(0)
        for i in range(len(p),len(s)):
            left=s[i-len(p)]
            sc[left]-=1
            if sc[left]==0:
                del sc[left]
            sc[s[i]]+=1
            if pc==sc:
                a.append(i-len(p)+1)
        return a