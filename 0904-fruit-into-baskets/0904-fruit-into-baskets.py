class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        a=0
        c=defaultdict(int)

        for r in range(len(fruits)):
            c[fruits[r]]+=1
            while len(c)>2:
                c[fruits[l]]-=1
                if c[fruits[l]]==0:
                    del c[fruits[l]]
                l += 1
            a=max(a,r-l+1)
        return a