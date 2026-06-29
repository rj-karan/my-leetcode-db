class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3: return n
        c=0
        p1=3
        p2=2
        for i in range(3,n):
            c=(p1+p2)
            p2=p1
            p1=c
        return c