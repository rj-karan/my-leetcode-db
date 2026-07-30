class Solution(object):
    def intersect(self,a,b):
        a=sorted(a)
        b=sorted(b)
        i=0
        j=0
        r=[]
        while i<len(a)and j<len(b):
            if a[i]<b[j]:
                i+=1
            elif b[j]<a[i]:
                j+=1
            else:
                r.append(a[i])
                i+=1
                j+=1
        return r