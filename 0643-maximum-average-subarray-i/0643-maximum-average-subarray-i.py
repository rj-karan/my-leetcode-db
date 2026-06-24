class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m=c=sum(nums[:k])
        for i in range(k,len(nums)):
            c+=nums[i]-nums[i-k]
            m=max(m,c)
        return m/k            