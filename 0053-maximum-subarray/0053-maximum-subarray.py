class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=float('-inf')
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            m=max(c,m)
            if c<0:
                c=0
        return m