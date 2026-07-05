class Solution:
    def isHappy(self, n: int) -> bool:
        s=[]
        while n not in s:
            s.append(n)
            t=0
            for i in str(n):
                t+=int(i)**2
            n=t
            if n==1:
                return True
        return False