class Solution:
    def largestInteger(self,nums,k):
        c={}
        for i in range(len(nums)-k+1):
            s=set(nums[i:i+k])
            for x in s:
                c[x]=c.get(x,0)+1
        a=-1
        for x in c:
            if c[x]==1:
                a=max(a,x)
        return a