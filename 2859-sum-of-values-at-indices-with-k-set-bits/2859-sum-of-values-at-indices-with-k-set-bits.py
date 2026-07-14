class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        a=0
        for i in range(len(nums)):
            b=bin(i)[2::]
            if b.count("1")==k:
                a+=nums[i]
        return a