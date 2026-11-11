class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            if len(mat) - 1 - i != i:
                sum += mat[i][len(mat) - 1 - i]
        return sum