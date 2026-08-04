class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        ma=max(nums)
        a=[]
        for i in range(m,ma+1):
            
            if i not in nums:
                a.append(i)
        return a
