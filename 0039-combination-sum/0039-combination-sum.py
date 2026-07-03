class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        total=0
        def backtrack(index,path,total):
            if total==target:
                r.append(path[:])
                return 
            if total>target or len(candidates)==index:
                return 
            path.append(candidates[index])
            backtrack(index,path,total+candidates[index])

            path.pop()
            backtrack(index+1,path,total)
        backtrack(0,[],0)
        return r