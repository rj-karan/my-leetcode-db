class Solution:
    def minimumPushes(self, word: str) -> int:
        f=sorted(Counter(word).values(), reverse=True)
        ans=0
        for i in range(len(f)):
            ans+=f[i]*((i//8)+1)
        return ans