class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        result = []
        mins = []
        maxs = []
        for i in range(n):
            mins.append(min(matrix[i]))
        for j in range(m):
            maxs.append(max([row[j] for row in matrix]))

        for i in maxs:
            if i in mins:
                result.append(i)
        return result