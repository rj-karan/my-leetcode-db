class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            c=list(words[i])
            l=0
            r=len(c)-1
            while l<r:
                c[l],c[r]=c[r],c[l]
                l+=1
                r-=1
            x="".join(c)
            if words[i]==x:
                return words[i]
        return ""