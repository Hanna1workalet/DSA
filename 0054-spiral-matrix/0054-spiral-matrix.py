class Solution:
    def spiralOrder(self, matrix):
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):         
                res.append(matrix[top][c])
            for r in range(top + 1, bottom + 1):      
                res.append(matrix[r][right])
            if top < bottom and left < right:        
                for c in range(right - 1, left - 1, -1):  
                    res.append(matrix[bottom][c])
                for r in range(bottom - 1, top, -1):      
                    res.append(matrix[r][left])
            top += 1; bottom -= 1; left += 1; right -= 1
        return res