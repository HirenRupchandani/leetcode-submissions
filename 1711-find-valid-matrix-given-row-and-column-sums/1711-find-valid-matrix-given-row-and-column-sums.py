class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        matrix = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                mini = min(rowSum[i], colSum[j])
                matrix[i][j] = mini
                rowSum[i] -= mini
                colSum[j] -= mini
            
        return matrix
        
                