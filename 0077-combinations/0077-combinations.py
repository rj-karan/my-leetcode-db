class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r=[]
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        for i in combinations(nums,k):
            r.append(list(i))
        return r