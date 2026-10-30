class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        q=deque()
        
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1 ) and board[i][j]=='O':
                    q.append((i,j))
                    board[i][j]='S'

        while q:
            
            r,c=q.popleft()
            d=[(0,1),(1,0),(0,-1),(-1,0)]

            for dr,dc in d:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m and board[nr][nc]=='O':
                    board[nr][nc]='S'
                    q.append((nr,nc))
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'