class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.strip().split()
        w.reverse()
        return ' '.join(w)