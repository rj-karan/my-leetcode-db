class Solution:
    def floodFill(self, image, sr, sc, color):
        o=image[sr][sc]

        if o==color:
            return image

        v=[[0]*len(image[0]) for _ in range(len(image))]

        def backtrack(i, j):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
                return

            if v[i][j]:
                return

            if image[i][j]!=o:
                return

            v[i][j]=1
            image[i][j]=color

            backtrack(i+1,j)
            backtrack(i-1,j)
            backtrack(i,j+1)
            backtrack(i,j-1)
            
        backtrack(sr,sc)

        return image