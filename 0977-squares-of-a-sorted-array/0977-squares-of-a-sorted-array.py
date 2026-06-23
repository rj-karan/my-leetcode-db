class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        i=0
        j=len(nums)-1
        k=len(nums)-1
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                a[k]=nums[i]**2
                i+=1
            else:
                a[k]=nums[j]**2
                j-=1
            k-=1
        return a
            
        