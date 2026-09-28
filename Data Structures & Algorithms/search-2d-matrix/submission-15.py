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
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if matrix[row][mid] == target:
                return True

            if target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
