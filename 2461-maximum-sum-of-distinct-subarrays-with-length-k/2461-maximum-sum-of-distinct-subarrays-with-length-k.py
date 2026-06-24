class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        m=0
        s=0
        d=defaultdict(int)
        for i in range(k):
            d[nums[i]]+=1
            s+=nums[i]
        if len(d)==k:
            m=s
        for i in range(k,len(nums)):
            left=nums[i-k]
            s-=left
            d[left]-=1
            if d[left]==0:
                del d[left]
            d[nums[i]]+=1
            s+=nums[i]
            if len(d)==k:
                m=max(m,s)
        return m
