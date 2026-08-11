class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        t=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                t+=nums[i]
            else:
                break
        s=set(nums)
        while t in s:
            t+=1
        return t