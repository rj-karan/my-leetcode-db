class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        c=0
        for i in nums:
            c+=i
            a.append(c)
        return a