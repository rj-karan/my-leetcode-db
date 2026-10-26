class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        f=[0]*26
        for t in tasks:
            f[ord(t)-ord('A')]+=1
        f.sort()
        print(f)
        c=f[25]-1
        i=c*n
        print(i)
        for ii in range(24,-1,-1):
            i-=min(c,f[ii])
        i=max(0,i)
        print(i)
        return len(tasks)+i