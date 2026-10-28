class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        i=0
        def dfs(r,c):
            q=deque([(r,c)])

            while q:
                ro,co=q.popleft()
                d=[(0,1),(1,0),(-1,0),(0,-1)]
                for dr,dc in d:
                    nr,nc=dr+ro,dc+co
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc]='0'
                        q.append([nr,nc])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    i+=1
                    dfs(r,c)
        return i