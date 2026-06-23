class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices[:]
        prices.sort(reverse=True)
        if prices==p:
            return 0
        b=p[0]
        profit=0
        for i in range(1,len(p)):
            if p[i]<b:
                b=p[i]
            elif p[i]-b >profit:
                profit=p[i]-b
        return profit