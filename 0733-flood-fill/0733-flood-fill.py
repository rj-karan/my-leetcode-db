class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        x=image[sr][sc]

        if x==color:
            return image
        
        
        m,n=len(image),len(image[0])
        q=deque([(sr,sc)])
        image[sr][sc]=color
        
        while q:
            r,c=q.popleft()
            for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                i,j=r+a,c+b
                if 0<=i<m and 0<=j<n and image[i][j]==x:
                    image[i][j]=color
                    q.append((i,j))
        
        return image