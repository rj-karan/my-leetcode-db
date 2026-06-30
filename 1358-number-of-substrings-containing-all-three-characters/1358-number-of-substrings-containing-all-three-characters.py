class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l={'a':-1,'b':-1,'c':-1}
        c=0
        for i,ch in enumerate(s):
            l[ch]=i
            if -1 not in l.values():
                c+=min(l.values()) + 1
        return c