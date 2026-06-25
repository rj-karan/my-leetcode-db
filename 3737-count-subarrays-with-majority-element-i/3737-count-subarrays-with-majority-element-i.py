class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        a=0
        k=[]
        for i in range(len(nums)):
            c=0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    c+=1
                l=j-i+1
                if c*2>l:
                    a+=1
        return a
