class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        a=0
        m=0
        for i in range(k):
            a+=arr[i]
        if a/k>=threshold:
            m+=1
        for r in range(k,len(arr)):
            l=r-k
            a-=arr[l]
            a+=arr[r]
            if a/k>=threshold:
                m+=1
        return m