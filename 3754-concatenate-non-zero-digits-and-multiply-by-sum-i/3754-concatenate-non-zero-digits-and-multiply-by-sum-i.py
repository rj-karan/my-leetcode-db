class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        n=list(str(n))
        t=""
        for i in n:
            if i !='0':
                t+=i
        s=sum(list(map(int,t)))
        k=int(t)*s
        return k