class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        a=s.add
        for n in nums:
            if n in s:
                return True
            a(n)
        return False