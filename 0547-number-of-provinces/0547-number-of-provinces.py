class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        g = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    g[i].append(j)
        vis=set()
        count=0
        for i in range(n):
            if i not in vis:
                count+=1
                vis.add(i)
            q=deque([i])
            while q:
                n=q.popleft()
                for y in g[n]:
                    if y not in vis:
                        vis.add(y)
                        q.append(y)

        return count