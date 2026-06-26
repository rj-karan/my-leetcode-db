class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m=0
        w=0
        for i in range(k):
            if blocks[i]=="W":
                m+=1
        w=m
        for r in range(k,len(blocks)):
            l=r-k
            if blocks[l]=="W":
                w-=1
            if blocks[r]=="W":
                w+=1
            m=min(m,w)
        return m
