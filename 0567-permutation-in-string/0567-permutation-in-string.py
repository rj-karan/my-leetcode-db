class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1c=defaultdict(int)
        s2c=defaultdict(int)
        for i in range(len(s1)):
            s1c[s1[i]]+=1
            s2c[s2[i]]+=1
        if s2c==s1c:
            return True
        for i in range(len(s1),len(s2)):
            left=s2[i-len(s1)]
            s2c[left]-=1
            if s2c[left] == 0:
                del s2c[left]
            s2c[s2[i]]+=1
            if s1c==s2c:
                return True
        return False