class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        b=count['b']
        a=count['a']
        l=count['l']//2 
        o=count['o']//2   
        n=count['n']
        return min(b,a,l,o,n)