class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        t=[]
        for i in range(len(matrix)):
    
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    t.append([i,j])
                
        for c,r in t:
            for j in range(len(matrix[0])):
                matrix[c][j]="#"  
            for i in range(len(matrix)):
                matrix[i][r]="#" 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="#":
                    matrix[i][j]=0
                