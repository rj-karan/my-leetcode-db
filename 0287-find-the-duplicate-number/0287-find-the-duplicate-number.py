class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k = len(nums)-len(set(nums))
        return (sum(nums)-sum(set(nums)))//k