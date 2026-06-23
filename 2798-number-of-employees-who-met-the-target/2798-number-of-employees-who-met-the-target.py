class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in hours:
            if target<=i:
                c+=1
        return c