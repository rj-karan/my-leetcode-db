class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        f=nums[-1]
        s=nums[-2]
        return ((f-1)*(s-1))