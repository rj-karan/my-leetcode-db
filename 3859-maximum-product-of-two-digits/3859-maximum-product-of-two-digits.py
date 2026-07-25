class Solution:
    def maxProduct(self, n: int) -> int:
        k=list(map(int,str(n)))
        k.sort()
        return k[-1]*k[-2]