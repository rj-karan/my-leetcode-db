class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        so=n**2
        se=n*(n+1)
        return math.gcd(so,se)