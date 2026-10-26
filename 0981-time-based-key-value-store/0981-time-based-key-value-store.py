class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr=self.store.get(key,[])
        l,h=0,len(arr)-1
        r=""
        while l<=h:
            m=(l+h)//2
            if arr[m][0]<=timestamp:
                r=arr[m][1]
                l=m+1
            else:
                h=m-1
        return r


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)