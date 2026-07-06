class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c=1
        p=intervals[0]
        for i in intervals[1:]:
            if  (p[1]<i[1]):
                print(i)
                c+=1
                if p[0]==i[0]:
                    c-=1
                p=i
           
        return c
            