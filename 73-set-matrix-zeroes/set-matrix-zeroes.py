class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c =  len(matrix[0])
        r_t=[0 for _ in range(r)]
        c_t=[0 for _ in range(c)]

        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    r_t[i]=-1
                    c_t[j]=-1
        
        for i in range(0,r):
            for j in range(0,c):
                if r_t[i]==-1 or c_t[j]==-1:
                    matrix[i][j]=0
