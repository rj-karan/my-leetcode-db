class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_num=sum(ord(x) for x in s)
        t_num=sum(ord(y) for y in t)
        return chr(t_num-s_num)