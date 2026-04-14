class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1
        while l <= r:
            m = (l+r) // 2
            row = m//n
            col = m%n

            if target == matrix[row][col]:
                return True 

            if target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1

        return False
        
        