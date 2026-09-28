class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = 0

        while l <= r:
            row = (r - l) // 2 + l

            if target < matrix[row][0]:
                r = row - 1
            elif target > matrix[row][-1]:
                l = row + 1
            else:
                break

        l = 0
        r = len(matrix[row]) - 1
                
        while l <= r:
            m = (r - l) // 2 + l

            if matrix[row][m] == target:
                return True

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
        
        return False