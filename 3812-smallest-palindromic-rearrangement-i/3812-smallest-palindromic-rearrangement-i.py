class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d={}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        left = ""
        mid = ""

        for ch in sorted(d):
            left += ch * (d[ch] // 2)
            if d[ch] % 2:
                mid = ch

        return left + mid + left[::-1]