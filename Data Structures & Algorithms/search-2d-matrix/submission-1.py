class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i  in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1

            while l <= r:
                mid = (l + r) // 2
                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

        